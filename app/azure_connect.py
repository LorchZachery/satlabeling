import os
from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.core.exceptions import ResourceNotFoundError
from azure.storage.blob import generate_blob_sas, BlobSasPermissions
from azure.storage.blob import generate_container_sas, ContainerSasPermissions
from osgeo import gdal
   
    
class Azure_Connect:
    """
    Connects to the storage container where all the satalite files are
    """
    def __init__(self, container_name):
        print("Connecting to "+container_name+" azure container")
        self.connect_str = os.getenv('AZURE_SCIHUB_CONNECTION_STRING')
        
        # Create the BlobServiceClient object which will be used to create a container client
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)
        self.container_name = container_name
        self.container_client = self.blob_service_client.get_container_client(self.container_name)
    
    def get_file_info(self):
        print("\nObtaining blob Info...")
        
        # List the blobs in the container
        blob_list = self.container_client.list_blobs()
        
        self.blob_files = []
        self.UTMs = []
        self.Years = []
        self.Dates = []
        self.Files = []
        for blob in blob_list:
            if blob.content_settings["content_type"] is not None:
                
                fname = blob.name
                list = fname.split('/')
                exclude = ['cloud','shadow']
                if exclude[0] not in list[3] and exclude[1] not in list[3]:
                    self.blob_files.append(blob)
                    
                    if list[0] not in self.UTMs:
                        self.UTMs.append(list[0])
                    year = list[0] + '/' + list[1]
                    if year not in self.Years:
                        self.Years.append(year)
                    date = year + '/' + list[2]
                    if date not in self.Dates:
                        self.Dates.append(date)
                    file = date + '/' + list[3]
                    if file not in self.Files:
                        self.Files.append(file)
        gdal.SetConfigOption('AZURE_STORAGE_CONNECTION_STRING', self.connect_str)
        self.Paths = []
        for blob in self.blob_files:
            path = '/vsiaz/' + self.container_name + '/' + blob.name
            self.Paths.append(path)
        print("\nBlob info obtained!")
    def get_paths(self):
        return self.Paths
    def get_UTMs(self):
        return self.UTMs
    def get_years(self):
        return self.Years
    def get_dates(self):
        return self.Dates
    def get_files(self):
        return self.Files



class Azure_Upload:
    """
    Uploads an image to the azure storgae container
    not yet universal
    """
    def __init__(self, container_name):
        print("Connecting to "+container_name+" azure container")
        self.connect_str = os.getenv('AZURE_SATLABELING_CONNECTION_STRING')
        
        # Create the BlobServiceClient object which will be used to create a container client
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)
        self.container_name = container_name
        self.container_client = self.blob_service_client.get_container_client(self.container_name)
        self.account_name = "satlabelingdata"
        self.account_key = os.getenv('AZURE_SATLABELING_ACCOUNT_KEY')
        self.container_name = "imagebands/uploads"
    def upload_file(self,path,name):
        self.blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=name)
        #print(self.blob_client.get_blob_properties())
        if not self.exists(name):
            print("\nUploadind Blob")
            
            with open(path, "rb") as data:
                self.blob_client.upload_blob(data)
        else:
            print("file already created")
    
    
    def exists(self,name) ->bool:
        # if the blob exists this will return true
        blob_client = self.blob_service_client.get_blob_client(container=self.container_name, blob=name)
        try:
            blob_client.get_blob_properties()
        except ResourceNotFoundError:
            return False
        return True
        
        
        
    def get_img_url_with_blob_sas_token(self,blob_name):
        """
        this function generates the sas token to display the blob
        on the webpage by making the url
        """
        blob_sas_token = generate_blob_sas(
            account_name=self.account_name,
            container_name=self.container_name,
            blob_name=blob_name,
            account_key=self.account_key,
            permission=ContainerSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=1)
        )
        blob_url_with_blob_sas_token = f"https://{self.account_name}.blob.core.windows.net/{self.container_name}/{blob_name}?{blob_sas_token}"
        return blob_url_with_blob_sas_token    
        
        
        