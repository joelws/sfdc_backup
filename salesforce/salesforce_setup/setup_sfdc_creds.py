# Setup SFDC Auth 
from cryptography.fernet import Fernet 
import json

# Generate Ferent key to encrypt SFDC Credentials 
def generate_key():
    '''
    Generates a key and saves it to a file 
    '''
    # Generate Fernet Key 
    key = Fernet.generate_key()
    with open('salesforce.key', 'wb') as key_file:
        key_file.write(key)

# Load generated key 
def load_key():
    '''
    Load the generated key 
    '''
    return open('salesforce.key', 'rb').read()


# Encrypt SFDC Credentials based on input 
def encrypt_sfdc_creds():
    '''
    Encrypts SFDC Creds and stores the as a json 
    '''

    # Get user input for Salesforce Auth 
    sf_username = input('sf_username')
    sf_password = input('sf_password')
    sf_token = input('sf_token')

    # Import ferent key and init fernet 
    try:
        # Try to load the fernet key 
        key = load_key()
    except:
        # If it doesn't exist, generate the encryption key 
        generate_key()
        key = load_key() 

    f = Fernet(key)

    # Convert inputs to bytes 
    sf_username = str(sf_username).encode()
    sf_password = str(sf_password).encode()
    sf_token = str(sf_token).encode()

    # Create encrypted sfdc auth obj 
    sfdc_auth_obj = {
        'sf_username' : f.encrypt(sf_username).decode(),
        'sf_password' : f.encrypt(sf_password).decode(),
        'sf_token' : f.encrypt(sf_token).decode()
    }

    # Convert SFDC Encrypted Auth to JSON 
    with open('sfdc_auth.json', 'w') as f:
        json.dump(sfdc_auth_obj, f)


if __name__=='__main__':
    encrypt_sfdc_creds()