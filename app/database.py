from azure.cosmos import exceptions, CosmosClient, PartitionKey
import azure.cosmos.partition_key as partition_key
import os

class Database:

    def __init__(self):
        # Initialize the Cosmos client
        self.endpoint = os.getenv('AZURE_DATABASE_URL')
        self.key = os.getenv('AZURE_DATABASE_KEY')
        
        # <create_cosmos_client>
        client = CosmosClient(self.endpoint, self.key)
        # </create_cosmos_client>
        
        # Create a database
        # <create_database_if_not_exists>
        database_name = 'satlabelingdb'
        database = client.create_database_if_not_exists(id=database_name)
        # </create_database_if_not_exists>
        
        # Create a container
        # Using a good partition key improves the performance of database operations.
        # <create_container_if_not_exists>
        container_name = 'labelinfo'
        self.container = database.create_container_if_not_exists(
            id=container_name, 
            partition_key=PartitionKey(path="/info"),
            offer_throughput=400
        ) 
        print("database initilized")    
    def add_data(self,image_name,section,label):
        image_info = self.get_image_info_json(image_name,section,label)
        read_item = self.exists(image_name)
        if read_item:
            self.container.replace_item(item=read_item, body=image_info)
        else:
            self.container.create_item(body=image_info)
        print("updated datbase")
    
    
    def get_image_info_json(self,image_name, section, label):
        image_info = {
        'id': image_name,
        'section': section,
        'label': label
    }
        return image_info

    def exists(self,image_name):
        try:
            
            read_item = self.container.read_item(item=image_name, partition_key=partition_key.NonePartitionKeyValue)
            
        except exceptions.CosmosResourceNotFoundError:
            return False
        return read_item
            
    def check_label(self,id):
        query = "SELECT c.label FROM c WHERE c.id = '" + id + "'"
        items = list(self.container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        
        if len(items) > 0:
            
            return items[0].get("label","error")
        else:
            return "No label"
        
        
        
            
            
            
            
            
            
            
            
            
