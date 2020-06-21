#!/bin/zsh

current_dir="$(pwd)"
venv_dir=/home/quentin/venv_list/yt_upload/
script_file=/home/quentin/gdrive/dev/python/boulot_utils/yt_upload/upload_folder.py

# activate the virtual environment
cd $venv_dir
source venv/bin/activate

# move back to previous directory
cd $current_dir

# start the script
python3 $script_file "$@"
#python3 /home/quentin/gdrive/dev/python/boulot_utils/yt_upload/upload_folder.py
