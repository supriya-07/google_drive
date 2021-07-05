###########################################################################################

#Purpose of the script

#############################################################################################################

#1.This script has been designed to write python test scripts 
#for google-drive to create,list,get,update,delete, trash and copy methods.

#############################################################################################################

import sys
import requests
from quickstart import main
drive_service = main()
###############################################################################################################

#Python Function whether Creating or not
def files_create():
    file_metadata = {
    'name': 'file_file',
    'description':'application',
    'starred': True
    }
    file = drive_service.files().create(body=file_metadata,
                                            fileId='id').execute()
    print ('File ID: %s' % file.get('id'))
    return file

#Python code to list
def files_list():
    files = drive_service.files().list(q="not name contains 'cache' ").execute()
    files_id = []
    files_name = []
    files = files.get('files')
    for file in files:
        files_id.append(file["id"])
        files_name.append(file["name"])
    return files_id,files_name

#Python code to get
def files_get(id):
    get_files = drive_service.files().get(fileId=id).execute()
    return get_files

#python code to delete
def files_delete(id):
    delete_file =drive_service.files().delete(fileId=id).execute()
    return 'deleted the file'

#Python code to emptytrash    
def files_emptyTrash():
    emptyTrash= drive_service.files().emptyTrash().execute()
    return emptyTrash

# def files_update(id):
#     files_update =drive_service.files().get(fileId=id).execute()
#     files_update['name']='Murali79.txt'
    
#     return files_update

# Python code to copy
def files_copy():
    file_id ='15nm843fVAlH6JNFEGJP0-tlOIkiDkk-v'
    folder_id='10EMRS7TRpbjM4wVfP9xIIt_PJomnaIdd'
    title = 'pic'
    # file_metadata ={
    #     'name':"baby_sticker",
    #     'discription':'application',
    #     'parents': folder_id,
    #     'starred': True
    # }
    drive_service.files().copy(fileId=file_id, body={"parents": [{"kind": "drive#fileLink",
                                 "id": folder_id}], 'title': title}).execute()
    return 'copied'

#Python code to export
def files_export():
    file_id ='1uvUrAPjbWCVKZdJFSPGa1kkihKQeosnQSXKvpMWWPOo' # Given word id 
    byteData =drive_service.files().export_media(fileId=file_id, mimeType='application/pdf').execute()
    # Here we converting word to pdf format
    with open ('murali.pdf','wb') as f:
        f.write(byteData)
    return 'successfully exported'
        
   
#Driver code to call the functions
print(files_export())
print(files_create())
print(files_list())
print(files_get('1QZGQndHUkYWO8aU3JIn5GSPmBsOl8UBu'))
# print(files_delete('1b4MoHfhJLMrRKGHg0fBjWnBKMfE9hyJJ'))
print(files_update('1uvUrAPjbWCVKZdJFSPGa1kkihKQeosnQSXKvpMWWPOo'))
print(files_copy())
print(files_emptyTrash())

############################################### Script Details ###############################################################

#Script name                            :   check.py
#Script ersion                          :   1.0
#Created by                             :   supriya.jakkamputi@infinite.com
# Create Date                           :   23/06/2021
# Last Modification Date                :   26/06/2021
