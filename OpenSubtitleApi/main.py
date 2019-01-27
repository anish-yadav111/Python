import os
import hashVideo
import openSubtitle



videoPath = "/media/anish/New Volume/movies/Suicide Squad 2016 English [700Mbdownload.in] EXTENDED 720p BRRip.mkv"
name = videoPath.split('/')[-1].split('.')[0]
print(name)


videoSize = os.path.getsize(videoPath)

videoHash = hashVideo.calc_file_hash(videoPath)

Subtitle = openSubtitle.OpenSubtitle(videoHash, videoSize, name)
Subtitle.Login()

if Subtitle.CheckMovieHash() != 'Error':

    print (" Downloading")


    if Subtitle.SearchSubtitles(1) != 'Error':
        Subtitle.DownloadSubtitles()

    if Subtitle.SearchSubtitles(2) != 'Error':
        Subtitle.DownloadSubtitles()

    if Subtitle.SearchSubtitles(3) != 'Error':
        Subtitle.DownloadSubtitles()

    if Subtitle.SearchSubtitles(4) != 'Error':
        Subtitle.DownloadSubtitles()

    if Subtitle.SearchSubtitles(5) != 'Error':
        Subtitle.DownloadSubtitles()
    
    



