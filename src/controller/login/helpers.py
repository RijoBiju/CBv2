import requests, base64, pickle
from pathlib import Path
import constants

def login(username: str, password: str) -> bool:
    response = requests.post('https://cbauth.herokuapp.com/', data={'discord':'{}'.format(username), 'password':'{}'.format(password)})
    if response.text == 'passed':
        return True
    else:
        return False

def encode_password(password: str) -> bytes:
    return base64.b64encode(password.encode('utf-8'))

def save_user_details(username: str, password: str) -> None:
    details = [username, encode_password(password)]
    with open(constants.SETTINGS_FILE_LOCATION, 'wb') as settings_file:
        pickle.dump(details, settings_file)