import os
import hashVideo
import openSubtitle


videoPath = input()

name = videoPath.split('/')[-1]
path = videoPath.split('/')
downloadPath = "/".join(path[0:len(path)-1])

videoSize = os.path.getsize(videoPath)

videoHash = hashVideo.calc_file_hash(videoPath)

Subtitle = openSubtitle.OpenSubtitle(videoHash, videoSize, name)
Subtitle.Login()

if Subtitle.CheckMovieHash() != 'Error':

    print (" Downloading")


    if Subtitle.SearchSubtitles(1) != 'Error':
        Subtitle.DownloadSubtitles(downloadPath)

    if Subtitle.SearchSubtitles(2) != 'Error':
        Subtitle.DownloadSubtitles(downloadPath)

    if Subtitle.SearchSubtitles(3) != 'Error':
        Subtitle.DownloadSubtitles(downloadPath)

    if Subtitle.SearchSubtitles(4) != 'Error':
        Subtitle.DownloadSubtitles(downloadPath)

    if Subtitle.SearchSubtitles(5) != 'Error':
        Subtitle.DownloadSubtitles(downloadPath)
  
else :
    print("Sorry Could Not Found It : (")  
    



