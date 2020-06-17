# Youtube Uploader


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

## Sources

[video category list](https://gist.github.com/dgp/1b24bf2961521bd75d6c)
[gfg upload](https://www.geeksforgeeks.org/youtube-data-api-playlist-set-2/)
