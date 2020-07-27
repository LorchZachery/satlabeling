import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from osgeo import gdal
   
    
class Azure_Connect:
    
    def __init__(self, container_name):
        print("Connecting to "+container_name+" azure container")
        self.connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        
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
    
        