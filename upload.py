import logging
import os
import sys
import time

# sets up the current directory to be the same as the .py file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
logging.debug(os.getcwd())

# start logging
logging.basicConfig(filename='python.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('Program started')

from rmapy.document import ZipDocument
from rmapy.api import Client

logging.debug('import of rmapy successful')

# sets up the remarkable api
logging.debug('setting up api')
rm=Client()
logging.debug('client set up successfully')
rm.renew_token()
logging.debug('api set up successfully')

# find the file
for arg in sys.argv[1:]:
    logging.debug(str(arg))
    # upload and log if file couldn't be found
    if os.path.exists(arg):
        rawDocument = ZipDocument(doc=arg)
        rm.upload(rawDocument)
        os.remove(arg)
    else:
        logging.debug("File doesn't seem to exist...")




