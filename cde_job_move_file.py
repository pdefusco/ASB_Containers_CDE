#https://pypi.org/project/azure-storage-blob/

from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobClient

#Enter your connection string here:
connection_string = "DefaultEndpointsProtocol=https;AccountName=xxxx;AccountKey=xxxx;EndpointSuffix=core.windows.net"
service = BlobServiceClient.from_connection_string(conn_str=connection_string)

file_name = "myfile_1.py"
cde_resource_path =

#Create a container
source_container_name = "my_source_container"
container_client = ContainerClient.from_connection_string(conn_str=connection_string, container_name=source_container_name)
container_client.create_container()

#Upload a file
blob = BlobClient.from_connection_string(conn_str=connection_string, container_name="my_container", blob_name="my_blob")

with open("/app/mount/myfile_1.py", "rb") as data:
    blob.upload_blob(data)

#Create other container
target_container_name = "my_target_container"
container_client = ContainerClient.from_connection_string(conn_str=connection_string, container_name=target_container_name)
container_client.create_container()

#Target
copied_blob = blob_service_client.get_blob_client(target_container_name, file_name)
copied_blob.start_copy_from_url(source_blob)
