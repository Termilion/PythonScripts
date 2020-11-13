from termcolor import colored
from pathlib import Path
import pytube as yt
import os

os.system('color')

path = input(colored("Enter path to destination: ", "yellow"))
link = input(colored("Enter link to playlist or video: ", "yellow"))

failedUrls = []

Path(path).mkdir(exist_ok=True)
if "&list=" in link:
    print("Fetching video URLs of playlist: %s" % (link))
    playlist = yt.Playlist(link)
    for i, url in enumerate(playlist):
        try:
            print("Downloading video %d: %s" %(i+1, url))
            yt.YouTube(url).streams.filter(file_extension='mp4').order_by("resolution").desc().first().download(path)
            print(colored("Finished download of video %d: %s" %(i+1, url), "green"))
        except:
            print(colored("Error downloading video: " + url, "red"))
            failedUrls.append(url)
else:
    try:
        print("Downloading video: %s" % (link))
        yt.YouTube(link).streams.filter(file_extension='mp4').order_by("resolution").desc().first().download(path)
        print(colored("Finished download of video %d: %s" %(i+1, url), "green"))
    except:
        print(colored("Error downloading video: " + link, "red"))
        failedUrls.append(link)

if len(failedUrls) > 0:
    failListFile = open("%s/failed.txt" % (path), "w")
    for url in failedUrls:
        failListFile.write(url + "\n")