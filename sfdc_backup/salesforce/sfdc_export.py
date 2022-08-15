# import libraries 
from sfdc_backup.salesforce.salesforce_setup.salesforce_setup import MySalesforce
from sfdc_backup.multi_threading.multi_threading import multi_threaded_req

import pandas as pd 

def get_schema():
    '''
    Gets the list of objects and their fields and creates a dictionary of the schema. 

    Format: 
    object_name : [List of Field Names]
    '''
    
    def get_fields()
        '''
        Function to get all fields from an object returned as a list
        '''
        fields = MySalesforce.sf.__dir__[object].describe()['fields']
        # return fields list 
        return fields

    # get list of Salesforce Objects
    objects = pd.DataFrame.from_records(MySalesforce.sf.describe()['sobjects']).name.tolist() 

    # schema dictionary col var
    schema = {} 

    

    objects_res = multi_threaded_req(objects, )

    for object in objects:  
        # get list of fields for that object
        fields = MySalesforce.sf.Account.describe()['fields']
        # field list col var 
        field_list = []
        # unpack fields 
        for field in fields:
            # append all the field names 
            field_list.append(field)
        # create dictionary record of object 
        schema[object] = field_list

    return schema


print(get_schema())

