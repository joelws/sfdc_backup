# import libraries 
from sfdc_backup.salesforce.api import sfdc_api, result_to_dataframe
from sfdc_backup.salesforce.schema import get_schema
from sfdc_backup.helper.multi_threading import multi_threaded_req

import pandas as pd 

def get_sfdc_tables(object_list : list):
    '''Gets a dictionary of DataFrames from a list of objects to query
    
    Params:
    - object_list : list
        - List of objects to get DataFrames for'''

    schema = get_schema(object_list)

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
            data = result_to_dataframe(sfdc_api.query_all(query))
            # return (object name, data) tuple 
            return object_name, data 

        # # query all objects 
        query_res = multi_threaded_req(query_object, queries.keys())

        return query_res
    
    table_dict = dict(map(lambda table: table.result(), query_objects(schema)))

    return table_dict