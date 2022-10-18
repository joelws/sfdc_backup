# import libraries 
from audioop import mul
from sfdc_backup.salesforce.setup.salesforce_setup import MySalesforce
from sfdc_backup.multi_threading.multi_threading import multi_threaded_req

import pandas as pd 

def get_schema():
    '''
    Gets the list of objects and their fields and creates a dictionary of the schema. 

    Format: 
    object_name : [List of Field Names]
    '''
    
    def get_fields(object):
        '''
        Function to get all fields from an object returned as a list
        '''
        # desc = MySalesforce.sf.Domain__c.describe()
        desc = getattr(MySalesforce.sf, object).describe()
        # check if queryable 
        if desc['queryable'] == False : return None
        # get fields 
        fields = desc['fields']
        # return (object, fields) tuple 
        return (object, fields)

    def unpack_object_info(res):
        '''
        Unpack object res features into schema object 
        '''
        # unpack feature 
        result = res.result()
        # check if result is None Type 
        if result == None: return None 

        # unpack tuple 
        object = result[0]
        fields = result[1]

        # unpack field names
        field_list = list(map(lambda x: x['name'], fields))

        # append to schema 
        return (object, field_list)

    # schmea vol var 
    schema = {} 
        
    # get list of Salesforce Objects
    objects = pd.DataFrame.from_records(MySalesforce.sf.describe()['sobjects']).name.tolist() 

    # get list of object info features 
    objects_res = multi_threaded_req(get_fields, objects)
    # unpack object info and assign to schema 
    schema_list = list(map(unpack_object_info, objects_res))
    # unpack object data to schema dict 
    for object in schema_list:
        # skip item if None and not queryable 
        if object == None: continue
        # unpack object 
        schema[object[0]] = object[1]

    # select objects to backup 
    objects_to_backup = [
        'Account',
        'Contact',
        'Opportunity',
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
    ]
    # index and select backup objects 
    schema = pd.Series(schema).loc[objects_to_backup]

    # return schema 
    return schema

def query_objects(schema):
    '''
    Query all objects
    '''
    # create queries col var 
    queries = {}
    # loop through objects 
    for object in schema.keys():
        query = f"""
            SELECT
                {','.join(schema[object])}
            FROM 
                {object}
        """
        queries[object] = query 

    # query object 
    def query_object(object_name):
        # unpack query 
        query = queries[object_name]
        # query object 
        data = MySalesforce.sfdc_query(query)
        # return (object name, data) tuple 
        return object_name, data 

    # # query all objects 
    query_res = multi_threaded_req(query_object, queries.keys())

    return query_res

