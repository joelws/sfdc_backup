'''Module to Export SFDC Data to SQL'''
from datetime import datetime

import pandas as pd

from sfdc_backup.salesforce.sfdc_export import get_sfdc_tables

def sfdc_to_sql(object_list : list,connection : object, timestamp=True, **kwargs):
    '''Funciton that exports SFDC Tables to SQL via python SQL connection
    
    Params:
    - object_list : list
        - List of objects to backup
    - connection : object
        - SQL connection object
    - append_date : Bool = True
        - Append a timestamp of the export to the table
    - **kwargs for Pandas .to_sql'''
    
    table_dict = get_sfdc_tables(object_list)

    for table in table_dict:
        df = table_dict[table]

        # apply timestamp
        if timestamp == True:
            df['timestamp'] = datetime.now().timestamp()
            
        df.to_sql(
            name=table,
            con=connection,
            index=False,
            **kwargs
        )