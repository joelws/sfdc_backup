'''Module for the Salesforce API and Schema'''
import pandas as pd
from simple_salesforce import Salesforce

from sfdc_backup.salesforce import config


# init Salesforce API
sfdc_api = Salesforce(
    username=config.SF_USERNAME,
    password=config.SF_PASSOWRD,
    security_token=config.SF_TOKEN
)

def result_to_dataframe(res_obj : object):
    '''Converst SFDC API response object to Pandas DataFrame'''
    return pd.DataFrame.from_records(res_obj['records']).drop('attributes',axis=1)