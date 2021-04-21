from rmapy.api import Client

rmapy = Client()
rmapy.is_auth()
rmapy.register_device("fkgzzklrs") # enter your device code here 
rmapy.renew_token()
rmapy.is_auth()
