# std lib
import os

# google
import googleapiclient.discovery

# own
from utils import get_authenticated_service
from utils import CLIENT_SECRETS_FILE
from utils import SCOPES
from utils import TOKEN_PLAYLIST_FILE


def add_to_playlist(id_playlist, id_video):
    youtube = get_authenticated_service(
        CLIENT_SECRETS_FILE, TOKEN_PLAYLIST_FILE, SCOPES)

    request = youtube.playlistItems().insert(
        part="snippet",
        body={"snippet": {"playlistId": id_playlist,
                          "position": 0,
                          "resourceId": {
                              "kind": "youtube#video",
                              "videoId": id_video
                          }
                          }
              }
    )
    response = request.execute()
    return response
