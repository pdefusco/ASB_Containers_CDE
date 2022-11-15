#https://pypi.org/project/azure-storage-blob/
import os
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobClient

#Enter your connection string here:
connection_string = "DefaultEndpointsProtocol=https;AccountName=xxxx;AccountKey=xxxx;EndpointSuffix=core.windows.net"
file_path = "myfile_1.py"
cde_resource_path = "/app/mount"

upload_file_path = os.path.join(cde_resource_path, file_path)

blob_service_client = BlobServiceClient.from_connection_string(conn_str=connection_string)

source_container_name = "source_container"
target_container_name = "target_container"

container_client = blob_service_client.create_container(source_container_name)
container_client = blob_service_client.create_container(target_container_name)

blob_client = blob_service_client.get_blob_client(container=source_container_name, blob=file_path)
print("\nUploading to Azure Storage as blob:\n\t" + file_path)
with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)


account_name = "azure_account_name"
# Source
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
source_blob = (f"https://{account_name}.blob.core.windows.net/{source_container_name}/{file_path}")
# Target
copied_blob = blob_service_client.get_blob_client(target_container_name, upload_file_path)
copied_blob.start_copy_from_url(source_blob)
