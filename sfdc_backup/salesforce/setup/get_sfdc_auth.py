import json
from cryptography.fernet import Fernet 
from sfdc_backup.salesforce.setup.setup_sfdc_creds import load_key

def decrpt_sfdc_cred(encrypted_message):
    '''
    Decrypts encrypted SFDC credential as a string 
    '''
    # Import fernet key 
    key = load_key()
    # Init fernet 
    f = Fernet(key)
    # Encode string from JSON for fernet 
    encrypted_message = encrypted_message.encode()
    # Decrypt message 
    decrypted_message =  f.decrypt(encrypted_message)
    # return decrypted message as str 
    return decrypted_message.decode()

# Open SFDC Ecrypted Auth JSON 
with open('sfdc_auth.json') as f:
    sfdc_auth_encrypted = json.load(f)

# Create SFDC Auth Obj with unencrypted keys 
sfdc_auth = {
    'sf_username' : decrpt_sfdc_cred(sfdc_auth_encrypted['sf_username']),
    'sf_password' : decrpt_sfdc_cred(sfdc_auth_encrypted['sf_password']),
    'sf_token' : decrpt_sfdc_cred(sfdc_auth_encrypted['sf_token'])
}