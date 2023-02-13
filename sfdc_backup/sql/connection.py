'''Module to setup SQL Connection'''
import sqlalchemy as sa
from sqlalchemy.engine.url import URL
from sqlalchemy import orm as sa_orm

from sfdc_backup.sql import config

def get_engine():
    '''Returns authenticated SQL engine'''
    url = URL.create(
        drivername=config.SQL_DRIVER,
        host=config.SQL_HOST,
        port=config.SQL_PORT,
        database=config.SQL_DB,
        username=config.SQL_USERNAME,
        password=config.SQL_PASSWORD
    )

    return sa.create_engine(url)