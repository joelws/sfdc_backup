'''
Script to backup main SFDC Objects to feather files 

Backup Naming Convetion: 
objectName_timestampOfBackup.feather 

Objects Backed Up: 
'''
import os

from sfdc_backup.sql.to_sql import sfdc_to_sql
from sfdc_backup.sql.connection import get_engine



object_list = os.environ['OBJECT_LIST'].split(',')


if __name__=='__main__':
    sfdc_to_sql(object_list, connection=get_engine(), timestamp=True, if_exists='append')