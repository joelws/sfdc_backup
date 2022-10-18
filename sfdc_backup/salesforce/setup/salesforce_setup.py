import simple_salesforce
import pandas as pd
import os 

# Import SFDC Auth dict 
try: 
    from sfdc_backup.salesforce.setup.get_sfdc_auth import sfdc_auth
except:
    from sfdc_backup.salesforce.setup.setup_sfdc_creds import encrypt_sfdc_creds
    # Run Encrypt Salesforce Creds Function to init creds 
    encrypt_sfdc_creds()
    from sfdc_backup.salesforce.setup.get_sfdc_auth import sfdc_auth
 
class MySalesforce:
 
    # Create Salesforce auth client 
    sf = simple_salesforce.Salesforce(
    username=sfdc_auth['sf_username'],
    password=sfdc_auth['sf_password'],
    security_token=sfdc_auth['sf_token']
    ) 
 
    # Salesforce query function 
    def sfdc_query(query,is_sql_file=False):
        '''
        Queries salesforce using the simple_salesforce package
        Params: 
        - query: Type - string or filepath | SQL Query filepath or text input defined in a variable
        - is_sql_file: Type - Bool | mark true if it's a file, so that it will open. Defualt = FALSE in order to accept a string. 
        '''
        sf = MySalesforce.sf
 
        if is_sql_file == True:
 
            sfdc_sql_query = open(query).read()
 
            sf_object_data = sf.query_all(sfdc_sql_query)
 
            sf_object_df = pd.DataFrame(sf_object_data['records'])
 
            df = sf_object_df.drop('attributes', axis='columns')
 
            return df
 
        else: 
 
            sfdc_sql_query = query
 
            sf_object_data = sf.query_all(sfdc_sql_query)
 
            sf_object_df = pd.DataFrame(sf_object_data['records'])
 
            df = sf_object_df.drop('attributes', axis='columns')
            
            return df

