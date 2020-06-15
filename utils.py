import os
import pickle


import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def read_playlist_name(dirpath):
    return dirpath.split('/')[-1].replace('_', ' ')


def format_title(path):
    filename = os.path.basename(path).replace('_', ' ').split('.')[0]
    print(filename)
    return filename


def read_description(description, file):

    dirname = os.path.dirname(file)
    desc = read_from_file(dirname)
    if desc is not None:
        description = desc
    return description


def read_from_file(dirname, filename='/description.md'):
    try:
        path = dirname + filename
        with open(path) as f:
            content = f.read()
        return content
    except Exception as e:
        print(repr(e))


def get_authenticated_service(client_secrets_file, client_token_file, scopes):
    flow = InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = get_cred(client_secrets_file, client_token_file, scopes)

    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def get_cred(client_secrets_file, client_token_file, scopes):
    '''
    Returns the credentials for google calendar api

    @return service: (googleapiclient.discovery.Resource) le service passé
    '''
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(client_token_file):
        with open(client_token_file, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(client_token_file, 'wb') as token:
            pickle.dump(creds, token)
    return creds


if __name__ == '__main__':
    format_title('/mnt/nfs/media/Capture/aero_complexes_exo_p1_1.mkv')
