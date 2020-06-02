'''Uploading file...
Video id "DyFExhzTkNE" was successfully uploaded.'''
response_video =
{
    'kind': 'youtube#video',
    'etag': '"wdgS91PsEbtTfi20GmzFuZzYg2s/qB0JCoKYyPz6Wiwn6NJL6xSFuWk"',
    'id': 'DyFExhzTkNE',
    'snippet': {'publishedAt': '2020-06-02T18:42:02.000Z',
                'channelId': 'UCktDNsB-vB9pA6QXluZbJvQ',
                'title': 'aero complexes exo p1 1',
                'description': 'Test Description',
                'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/DyFExhzTkNE/default.jpg',
                                           'width': 120,
                                           'height': 90},
                               'medium': {'url': 'https://i.ytimg.com/vi/DyFExhzTkNE/mqdefault.jpg',
                                          'width': 320,
                                          'height': 180},
                               'high': {'url': 'https://i.ytimg.com/vi/DyFExhzTkNE/hqdefault.jpg',
                                        'width': 480,
                                        'height': 360}},
                'channelTitle': 'Quentin Konieczko',
                'categoryId': '27',
                'liveBroadcastContent': 'none',
                'localized': {'title': 'aero complexes exo p1 1',
                              'description': 'Test Description'}},
    'status': {'uploadStatus': 'uploaded',
               'privacyStatus': 'unlisted',
               'license': 'youtube',
               'embeddable': False,
               'publicStatsViewable': False,
               'selfDeclaredMadeForKids': False}
}


response_playlist = {'kind': 'youtube#playlist',
                     'etag': 'EeDQl0dVMn-MYU6hDNDlMbnvCFI',
                     'id': 'PLYCb2MMcjNSRhF7jU45zsIAi3Q_TJP6Jh',
                     'snippet': {'publishedAt': '2020-06-02T19:35:21Z',
                                 'channelId': 'UCktDNsB-vB9pA6QXluZbJvQ',
                                 'title': 'Sample playlist created via API',
                                 'description': 'This is a sample playlist description.',
                                 'thumbnails': {'default': {'url': 'http://s.ytimg.com/yts/img/no_thumbnail-vfl4t3-4R.jpg',
                                                            'width': 120,
                                                            'height': 90},
                                                'medium': {'url': 'http://s.ytimg.com/yts/img/no_thumbnail-vfl4t3-4R.jpg',
                                                           'width': 320,
                                                           'height': 180},
                                                'high': {'url': 'http://s.ytimg.com/yts/img/no_thumbnail-vfl4t3-4R.jpg',
                                                         'width': 480,
                                                         'height': 360}},
                                 'channelTitle': 'Quentin Konieczko',
                                 'tags': ['sample playlist',
                                          'API call'],
                                 'defaultLanguage': 'en',
                                 'localized': {'title': 'Sample playlist created via API',
                                               'description': 'This is a sample playlist description.'}},
                     'status': {'privacyStatus': 'private'}}
