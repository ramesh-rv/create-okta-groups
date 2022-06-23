# This script will create groups in the Okta org specified.
# This script uses Okta Python SDK under the hood. The script reads the group names from the groups.csv file and creates the groups in Okta.
# The log file will contain the updates of the groups created or skipped.

import asyncio
import csv
import json
import logging


from okta import models
from okta.client import Client as OktaClient
from okta.exceptions import OktaAPIException




logging.basicConfig(filename="group_create.log", format='%(levelname)s:%(asctime)s:%(message)s',
                    filemode='w', level=logging.INFO)
logging.info(' Execution started')
logging.info(' Reminder: To check the Okta Tenant Name and API Key are correct')




async def main():
    config = {'orgUrl': 'your-okta-org-here',
              'token': 'api-token-here',
              'raiseException': True}
    client = OktaClient(config)
    logging.info(f" Trying to connect to the Okta Tenant -  {config.get('orgUrl')} ")
    print ("Script will try to create the groups.Please check the log file for update")

    with open('groups.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            row_names = row.keys()
            row_items = row.items()
            group_list = str(row["GROUP_NAME"])
            
            client = OktaClient(config)
            try:
                group_profile = models.GroupProfile({
                    'name': group_list,
                    'description': "Groups created through script"
                })
                group_model = models.Group({
                    'profile': group_profile
                })
             # Create Group
                group_name, resp, err = await client.create_group(group_model)
                logging.info(f" Group {group_profile.name} created ")
            except OktaAPIException as err:
                logging.error(f'Error while creating group :  {group_list} || Message :{err.args[0]["errorCauses"][0]["errorSummary"]}')




asyncio.run(main())

# Deprecated 
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


