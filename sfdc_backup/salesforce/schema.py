'''Module that gets the SFDC Schema'''
import pandas as pd

from sfdc_backup.salesforce.api import sfdc_api, result_to_dataframe
from sfdc_backup.helper.multi_threading import multi_threaded_req


def get_schema(object_list : list):
    '''
    Returns the schema for the list of objects to backup

    Params:
    - object_list : list
        - List of objects that you'd like to back up

    Format: 
    object_name : [List of Field Names]
    '''
    
    def get_fields(object):
        '''
        Function to get all fields from an object returned as a list
        '''
        # desc = MySalesforce.sf.Domain__c.describe()
        desc = getattr(sfdc_api, object).describe()
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
    objects = pd.DataFrame.from_records(sfdc_api.describe()['sobjects']).name
    # filter objects list to only those requested 
    if object_list != None:
        objects = objects[objects.isin(object_list)].tolist()
    else:
        objects = objects.tolist()

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
    # return schema 
    return pd.Series(schema)