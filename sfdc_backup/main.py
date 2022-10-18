'''
Script to backup main SFDC Objects to feather files 

Backup Naming Convetion: 
objectName_timestampOfBackup.feather 

Objects Backed Up: 

'Account',
'Contact',
'Opportunity'
'Lead',
'Campaign',
'CampaignMember',
'OpportunityCompetitor', 
'OpportunityContactRole', 
'OpportunityFeed', 
'OpportunityFieldHistory', 
'OpportunityHistory', 
'OpportunityLineItem', 
'OpportunityLineItemSchedule', 
'OpportunityPartner', 
'OpportunityShare', 
'OpportunitySplit', 
'OpportunitySplitType', 
'OpportunityStage', 
'OpportunityTag', 
'OpportunityTeamMember'
'''

from datetime import datetime

from sfdc_backup.salesforce import sfdc_export 
from sfdc_backup.multi_threading.multi_threading import multi_threaded_req
from sfdc_backup.salesforce.setup.salesforce_setup import MySalesforce

import pandas as pd 


def backup_sfdc():
    # get SFDC Schema 
    schema = sfdc_export.get_schema()
    # get futures from multiple quereies 
    res = sfdc_export.query_objects(schema)
    # get now timestamp as file 
    now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    # function to unpack future results and store to Data to feathers 
    def unpack_results(res):
        # unpack results 
        res_list = list(
            map(
                lambda x: x.result(),
                res
            )
        )
        # backup object 
        for object in res_list: 
            # unpack object results tuple 
            object_name, object_data = object
            # store results 
            object_data.to_feather('./sfdc_backup/backup/' + object_name + '_' + now + '.feather')
    
    # unpack results 
    unpack_results(res)

# run SFDC Backup
backup_sfdc()