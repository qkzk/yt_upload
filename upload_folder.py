'''
1. créer une playlist depuis le dossier
2. upload dossier complet
3. ajouter éléments à la playlist
'''

# stdlib
import argparse
import os

# own
import color
from add_to_playlist import add_to_playlist
from create_playlist import create_playlist
from upload_video import upload_video


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
I will upload all .mkv files. They will be added to a playlist.

    {0}

    videos :
'''
WARN_INPUT = '\nDo you want to continue ? [y/N] : '
CHECK_USER_WANT_TO_FILTER_VIDEOS = "Do you want to filter those videos ? : "
MSG_ACTION_UPLOAD = "Upload this video ? : {} : "


def parse_playlist_and_directory():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d",
                        "--directory",
                        help="provide a path for the videos",
                        action="store",
                        type=str,
                        required=False,
                        dest='directory')
    parser.add_argument("-p",
                        "--playlist",
                        help="provide a playlist id",
                        action="store",
                        type=str,
                        required=False,
                        dest='playlist')
    args = parser.parse_args()
    # debugging
    # print(args)
    # print(args.playlist)
    # print(args.directory)
    if args.directory:
        directory = args.directory
        print("I'll use the provided directory:", directory)
    else:
        print("no directory provided, using cwd")
        directory = os.getcwd()
    if args.playlist:
        playlist_id = args.playlist
        print("I'll insert videos in this playlist:", playlist_id)
    else:
        print("no playlist_id provided, I'll create a new one")
        playlist_id = None

    return directory, playlist_id


def user_want_to_continue(directory, video_dict):
    color.print_color(WARN_MSG.format(directory), color="RED")
    color.print_color(', '.join(video_dict.keys()), color="YELLOW")
    return input(color.format_color(WARN_INPUT, color="CYAN")) in 'yY'


def create_video_dict(directory):
    return {video: True
            for video in sorted(os.listdir(directory), reverse=True)
            if video.endswith("mkv")}


def check_user_want_to_continue(directory, video_dict):
    if not user_want_to_continue(directory, video_dict):
        color.print_color("aborting... see you next time", color="RED")
        exit(0)


def check_playlist_valid(playlist_id):
    if playlist_id is None:
        color.print_color("Couldn't create the playlist. Aborting",
                          color="RED")
        exit(-1)


def check_user_want_to_filter_videos(video_dict):
    if input(color.format_color(CHECK_USER_WANT_TO_FILTER_VIDEOS,
                                color="RED")) in 'yY':
        video_dict = filter_videos_dict(video_dict)
    return video_dict


def filter_videos_dict(video_dict):
    for video_file in video_dict.keys():
        if input(color.format_color(MSG_ACTION_UPLOAD.format(video_file),
                                    color="YELLOW")) in 'nN':
            video_dict[video_file] = False
    return video_dict


def upload_all_videos(directory, video_dict):
    uploaded_video_ids = []
    failed_videos = []
    for video_file, action_upload in video_dict.items():
        if action_upload:
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
        except Exception:
            playlist_insert_failed.append(video_id)
            print("http error when trying to insert video to playlist")
            print("This video may be a duplicate or the playlist_id may be wrong")
    if playlist_insert_failed != []:
        color.print_color("Those playlist insertion have failed:", "YELLOW")
        color.print_color(", ".join(playlist_insert_failed), "RED")
    else:
        color.print_color(
            "Every video was successfully inserted into the playlist.",
            color="CYAN")


def upload_folder():
    print(WELCOME_MSG)
    directory, playlist_id = parse_playlist_and_directory()
    video_dict = create_video_dict(directory)
    check_user_want_to_continue(directory, video_dict)
    video_dict = check_user_want_to_filter_videos(video_dict)

    if playlist_id is None:
        # créer une playlist depuis le dossier courant
        playlist_id = create_playlist(directory)
    else:
        print("using provided playlist")
    check_playlist_valid(playlist_id)

    # upload toutes les vidéos du folder et récupérer leurs id
    uploaded_video_ids, _ = upload_all_videos(
        directory, video_dict)

    # ajouter les vidéos à la playlist
    insert_videos_playlist(uploaded_video_ids, playlist_id)


if __name__ == "__main__":
    upload_folder()
