#!/bin/zsh

current_dir="$(pwd)"
venv_dir=/home/quentin/venv_list/yt_upload/
script_file=/home/quentin/gdrive/dev/python/boulot_utils/yt_upload/

cd $venv_dir
source venv/bin/activate


cd $current_dir

python3 /home/quentin/gdrive/dev/python/boulot_utils/yt_upload/upload_folder.py
