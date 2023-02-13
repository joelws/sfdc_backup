'''Configuration Module for Salesforce API'''
import os

# dev setup
SF_USERNAME = os.environ['sf_username']
SF_PASSOWRD = os.environ['sf_password']
SF_TOKEN = os.environ['sf_token']

# for production get from docker secrets
# SF_USERNAME = open('/run/secrets/sf_username').read().replace('\n','')
# SF_PASSWORD = open('/run/secrets/sf_password').read().replace('\n','')
# SF_TOKEN = open('/run/secrets/sf_token').read().replace('\n','')