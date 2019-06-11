#from azure.storage import BlobService
from azure.storage.blob import BlockBlobService
import azure.common
import config as config
import base64
import datetime

blob_service = BlockBlobService(account_name=config.ACCOUNT_NAME, account_key=config.ACCOUNT_KEY)

#print (dir(blob_service))

blob_list=blob_service.list_blobs(container_name=config.CONTAINER_NAME)
for blob_name in blob_list:
    #print (blob_name.name)  #works
    #print (blob_name.properties.last_modified)  #works
    #print (blob_name.properties.content_length) #works
    i_uri = "https://{}.blob.core.windows.net/{}/{}".format(config.ACCOUNT_NAME,config.CONTAINER_NAME,blob_name.name)
    #print(uri)
    #https://blobtable4hacker3.blob.core.windows.net/website/website_docs/collateral/Dubai Brochure.pdf
    # URL and Filename Safe Base64 Encoding
    id_bytes = base64.urlsafe_b64encode(i_uri.encode("utf-8"))
    i_id = str(id_bytes, "utf-8")
    #print ("I am here")
    #print(type(blob_name.properties.last_modified))
    #print (blob_name.properties.last_modified.strftime('%d/%m/%y %I:%M %S %p'))
    i_last_modified = blob_name.properties.last_modified.strftime('%d/%m/%y %I:%M %S %p')
    i_size = str(blob_name.properties.content_length)

    #test_str = "{}\n{}\n{}\n{}\n{}\n".format(i_id,i_uri,blob_name.name,blob_name.properties.content_length,blob_name.properties.last_modified)
    #print (test_str)
    #break
    # set metadata to "myblob" of container "mycontainer"
    blob_service.set_blob_metadata(container_name=config.CONTAINER_NAME,
                                blob_name=blob_name.name,
                                metadata={"id":i_id,"url":i_uri,"file_name":blob_name.name,"size":i_size,"last_modified":i_last_modified})

#get metadata of "myblob" of container "mycontainer"
#metadata = blob_service.get_blob_metadata(container_name="website",blob_name="website_docs/collateral/Dubai Brochure.pdf")
#print (metadata)