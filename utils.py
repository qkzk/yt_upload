import os
import pickle


import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

CLIENT_SECRETS_FILE = "/home/quentin/gdrive/dev/python/boulot_utils/yt_upload/tokens/client_secret_785506707104-1ov3mff32p12b0dm7um4k4tcfic382cs.apps.googleusercontent.com.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

TOKEN_PLAYLIST_FILE = '/home/quentin/gdrive/dev/python/boulot_utils/yt_upload/tokens/upload_playlist_token.pickle'
TOKEN_VIDEO_FILE = '/home/quentin/gdrive/dev/python/boulot_utils/yt_upload/tokens/upload_video_token.pickle'

def read_playlist_name(dirpath):
    # print("read_playlist_name - dirpath", dirpath)
    return dirpath.split('/')[-1].replace('_', ' ')


def format_title(path):
    filename = os.path.basename(path).replace('_', ' ').split('.')[0]
    # print(filename)
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
        print("description file not found")
        # print(repr(e))


def get_authenticated_service(client_secrets_file, client_token_file, scopes):
    # flow = InstalledAppFlow.from_client_secrets_file(
        # client_secrets_file, scopes)
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
            # print("get_authenticated_service : creds found !")
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        # print("get_authenticated_service, creds not found or invalid")
        if creds and creds.expired and creds.refresh_token:
            # print("get_authenticated_service, creds expired ! refreshing...")
            creds.refresh(Request())
        else:
            # print("get_authenticated_service, creating creds...")
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(client_token_file, 'wb') as token:
            pickle.dump(creds, token)
        # print("get_authenticated_service, creds saved to", client_token_file)
    return creds


if __name__ == '__main__':
    format_title('/mnt/nfs/media/Capture/aero_complexes_exo_p1_1.mkv')
