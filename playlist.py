from time import time
from pytube import YouTube, Playlist
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_playlist():
    """
    Asks user for playlist title
    """

    

# playlist_link = "https://www.youtube.com/playlist?list=PLJKfZ_cKGyLdYqdzGLCJPbsi9UGCcEc5e"
playlist_link = "https://www.youtube.com/playlist?list=PLHtZ4BshlOJW8f5QAr9d3tOMcggdAmKgW"
video_links = Playlist(playlist_link).video_urls
start = time()


def get_video_title(link):
    title = YouTube(link).title
    return title


processes = []
with ThreadPoolExecutor(max_workers=10) as executor:
    for url in video_links:
        processes.append(executor.submit(get_video_title, url))

video_titles = []
for task in as_completed(processes):
    video_titles.append(task.result())
    print(task.result())


print(f'Time taken: {time() - start}')
