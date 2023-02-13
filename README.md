# Salesforce Backup Script 
- Service to backup specified tables to a SQL DB

## Authentication 

### sfdc-backup
- ENV variables required. See dev. compose file example
```
- SQL_DRIVER=postgresql
- SQL_HOST=db
- SQL_PORT=5432
- SQL_DB=salesforce-test
- SQL_USERNAME=postgres
- SQL_PASSWORD=password
- sf_username=${sf_username}
- sf_passowrd=${sf_password}
- sf_token=${sf_token}
- OBJECT_LIST=Opportunity, Account, Contact
```
- SFDC Token recieved via email when you reset your password. 
- OBJECT_LIST must be a string of comma separated values

## Running the service
- This is built to be run as a scheduled service to backup to a SQL DB. 
- Just schedule the Dockerfile to run with the approraite environment variables and you're good to go.
- Testing is done with postgres to mimic Redshift's Postgres setup

### Testing
- To dry run the service, you can use the docker-compose.dev.yml file which spins up a DB and runs a quick backup. For this I'd recommend testing with a minimal amount of objects to reduce testing time. 1 or 2 should work. 
