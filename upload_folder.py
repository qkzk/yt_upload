'''
1. créer une playlist depuis le dossier
2. upload dossier complet
3. ajouter éléments à la playlist
'''

# stdlib
import os
import sys

# own
from add_to_playlist import add_to_playlist
from create_playlist import create_playlist
from upload_video import upload_video

# import color
import importlib.util
spec = importlib.util.spec_from_file_location(
    "color",
    "/home/quentin/gdrive/dev/python/linux_utils/tests/colors.py")
color = importlib.util.module_from_spec(spec)
spec.loader.exec_module(color)


WELCOME_MSG = '''
\033[0;37;41m

                              #                          #               ##
 ###  ##                      #            ### ###       #                #
  #   #              #        #             #   #        #                #
   # #    ###  #  ## ## #  ## ####   ##     #   #  ####  #  ###   ##    ###
    #    #   # #   # #  #   # #   # #  #    #   #  #   # # #   #   ##  #  #
    #    #   # #   # #  #   # #   # ####    #   #  #   # # #   # ## # #   #
    #    #   # #   # #  #   # #  ## #       #  ##  #  ## # #   # #  # ##  #
   ###    ###   #### ##  #### ###    ###     ##    ###   #  ###   ###  ####
                                                   #
                                                   ##
\033[0m
'''

WARN_MSG = '''
I will upload all .mkv files and create a playlist from

    {0}

    videos :
'''
WARN_INPUT = '\nDo you want to continue ? [y/N] : '


def read_directory_from_args():
    if len(sys.argv) == 1:
        directory = os.getcwd()
    else:
        directory = sys.argv[1]
    return directory


def user_want_to_continue(directory, videos_list):
    print(WELCOME_MSG)
    color.print_color(WARN_MSG.format(directory), color="RED")
    color.print_color(', '.join(videos_list), color="YELLOW")
    return input(color.format_color(WARN_INPUT, color="CYAN")) in 'yY'


def create_videos_list(directory):
    return [video
            for video in sorted(os.listdir(directory), reverse=True)
            if video.endswith("mkv")]


def check_user_want_to_continue(directory, videos_list):
    if not user_want_to_continue(directory, videos_list):
        color.print_color("aborting... see you next time", color="RED")
        exit(0)


def check_playlist_valid(playlist_id):
    if playlist_id is None:
        color.print_color("Couldn't create the  playlist. Aborting",
                          color="RED")
        exit(-1)
    print("Playlist created successfully")


def upload_all_videos(directory, videos_list):
    uploaded_video_ids = []
    failed_videos = []
    for video_file in videos_list:
        response, _ = upload_video(os.path.join(directory, video_file))
        if response is not None:
            uploaded_video_ids.append(response["id"])
        else:
            failed_videos.append(video_file)
    if failed_videos != []:
        color.print_color("Those uploads have failed:", color="YELLOW")
        color.print_color(', '.join(failed_videos), color="RED")
    else:
        print("Every video was uploaded successfully.")
    return uploaded_video_ids, failed_videos


def insert_videos_playlist(uploaded_video_ids, playlist_id):
    playlist_insert_failed = []
    print("\nuploaded_video_ids", uploaded_video_ids, end='\n\n')
    for video_id in uploaded_video_ids:
        try:
            response = add_to_playlist(playlist_id, video_id)
            if not 'id' in response:
                playlist_insert_failed.append(video_id)
        except Exception as e:
            playlist_insert_failed.append(video_id)
            print("http error when trying to insert video to playlist")
            print("This video may be a duplicate")
    if playlist_insert_failed != []:
        color.print_color("Those playlist insert have failed:", "YELLOW")
        color.print_color(", ".join(playlist_insert_failed), "RED")
    else:
        color.print_color(
            "Every video was successfully inserted into the playlist.",
            color="CYAN")


def upload_folder():

    directory = read_directory_from_args()
    videos_list = create_videos_list(directory)
    check_user_want_to_continue(directory, videos_list)

    # créer une playlist depuis le dossier courant
    playlist_id = create_playlist(directory)
    check_playlist_valid(playlist_id)

    # upload toutes les vidéos du folder et récupérer leurs id
    uploaded_video_ids, failed_videos = upload_all_videos(
        directory, videos_list)

    # ajouter les vidéos à la playlist
    insert_videos_playlist(uploaded_video_ids, playlist_id)


if __name__ == "__main__":
    upload_folder()
