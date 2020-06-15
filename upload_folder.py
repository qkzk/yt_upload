'''
1. créer une playlist depuis le dossier
2. upload dossier complet
3. ajouter éléments à la playlist
'''
import os
from add_to_playlist import add_to_playlist
from create_playlist import create_playlist
from upload import upload_video


def upload_folder(directory=None):
    # créer une playlist depuis le dossier courant
    playlist_id = create_playlist(directory)
    # upload toutes les vidéos du folder et récupérer leurs id
    video_ids = []
    if directory is None:
        directory = os.getcwd()
    for video_file in sorted(os.listdir(directory)):
        if video_file.endswith(".mkv"):
            response, _ = upload_video(os.path.join(directory, video_file))
            video_ids.append(response["id"])
    # ajouter les vidéos à la playlist
    for video_id in video_ids:
        add_to_playlist(playlist_id, video_id)

