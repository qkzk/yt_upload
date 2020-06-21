# Youtube Uploader

## Description

This program allows you to upload a whole folder to youtube with 
a single command.

Some string coloring are used so it may prints strange characters
on non POSIX shells.

## Usage

0. You should be somewhat familiar with youtube (or google) API and know how to
    create a token.
1. call the script `python upload_folder.py` with or without arguments

    if no argument is provided, it will use the current folder as the playlist
    name.

    possible arguments are :

    `-d` or `--directory`: absolute path to the directory

    `-p` or `--playlist`: the already existing playlist_id you want to use.
    The playlist id is simply the URL of the playlist : 
    `https://www.youtube.com/playlist?list=THIS_IS_THE_PLAYLIST_ID`

2. The script will search for mkv videos in the directory. (next feature : all valid formats).
    It will also look for a file named `description.txt`. If found, its content
    will be added to the youtube video description.
3. It will ask confirmation, to avoid basic mistakes, showing you the list of 
    videos from the folder.
4. A second confirmation will ask you if you want to filter the videos.
    If you say yes, you will be able to select which video you want to upload 
    specifically.
5. Videos will be uploaded in their name order.
6. Some confirmations are printed, showing you what happened.


I made an alias `ytu` which activate my virtual environment and start the 
script with all passed parameters.

```bash
$  ytu -d /my/video/folder -p MYplaylistID
```

## French description, mostly for me

Uploader un dossier complet et créer une playlist directement bien rangée
avec mes paramètres par défaut

## Usage

1. cd dans le dossier contenant les vidéos. 
    *   Le nom du dossier est celui de la playlist
    *   Un fichier `description.txt` peut-être rempli, il servira de description
        pour toutes les vidéos et la playlist
    *   chaque vidéo (.mkv) du dossier sera uploadée
2. Lancer le script .sh sans paramètre (un alias est crée)


## Paramètres à définir

- [x] title: string
- [x] description: string
- [x] audience: not made for kids
- [x] catégorie: 27 (éducation)
- [ ] **comments: disabled** IMPOSSIBLE
- [x] users can view ratings: NO
- [x] allow embending: NO


## Todo


- [x]  connect
- [x]  retrieve
- [x]  upload
- [x]  upload with full description -- impossible de bloquer les comments
- [x]  upload batch to playlist
   - [x]   create playlist
   - [x]   upload whole folder
   - [x]   add each video to playlist
- [x]  organiser le tout dans un beau truc
- [x]  tester
- [ ]  multiples fortmats de videos, pas seulement mkv
- [ ]  détecter si les couleurs passent avant d'en mettre partout

## Sources

[video category list](https://gist.github.com/dgp/1b24bf2961521bd75d6c)
[gfg upload](https://www.geeksforgeeks.org/youtube-data-api-playlist-set-2/)
