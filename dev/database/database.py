from azure.cosmos import exceptions, CosmosClient, PartitionKey
import os

class Database:

    def __init___(image_name,section,label):
        # Initialize the Cosmos client
        endpoint = os.getenv('AZURE_DATABASE_URL')
        key = os.getenv('AZURE_DATABASE_KEY')
        
        # <create_cosmos_client>
        client = CosmosClient(endpoint, key)
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
        container = database.create_container_if_not_exists(
            id=container_name, 
            partition_key=PartitionKey(path="/info"),
            offer_throughput=400
        )  
        
        image_info = get_image_info_json(image_name,section,label)
        read_item = container.read_item(item=image_name, partition_key=key)
        if read_item:
            container.replace_item(item=read_item, boby=image_info)
        else:
            container.create_item(body=image_info)
        print("updated datbase")
    
    
    def get_image_info_json(image_name, section, label):
        image_info = {
        'id': image_name,
        'section': section,
        'label': label,
    }
        return image_info


