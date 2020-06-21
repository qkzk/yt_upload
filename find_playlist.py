from pprint import pprint
from utils import read_playlist_name
from utils import get_authenticated_service
from utils import CLIENT_SECRETS_FILE
from utils import SCOPES
from utils import TOKEN_PLAYLIST_FILE


def retrieve_playlist():
    client = get_authenticated_service(CLIENT_SECRETS_FILE,
                                       TOKEN_PLAYLIST_FILE, SCOPES)
    request = client.playlists().list(
        part="snippet,contentDetails",
        mine=True,
        maxResults=50,

    )
    response = request.execute()
    return response


if __name__ == "__main__":
    playlist_response = retrieve_playlist()
    pprint(playlist_response)
