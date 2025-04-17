import os

from pytubefix import YouTube
from pytube import Playlist


def read_urls_from_file(file_path):
    """
    Reads URLs from a text file.
    
    :param file_path: Path to the file containing the URLs.
    :return: List of URLs.
    """
    try:
        with open(file_path, "r") as file:
            urls = [line.strip() for line in file if line.strip()]
        return urls
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []


def download_videos(url_list, output_folder="."):
    """
    Downloads YouTube videos from a list of URLs and saves them as MP4 files.
    
    :param url_list: List of YouTube URLs.
    :param output_folder: Folder where the videos will be saved. Default is the current folder.
    """
    for url in url_list:
        try:
            print(f"Downloading: {url}")
            yt = YouTube(url)
            stream = yt.streams.filter(file_extension="mp4", progressive=True).get_highest_resolution()
            stream.download(output_folder)
            print(f"Video '{yt.title}'\033[0;32m downloaded successfully!\033[m")

        except Exception as e:
            print(f"Error downloading {url}: {e}")
            
while True:
    input_url = str(input('URL: ')) 

    input_file = str(input('my videos will be sent to the folder: '))

    # Playlist link
    playlist_url = input_url

    # Load the playlist
    playlist = Playlist(playlist_url)

    # Output file
    output_playlist = "urls.txt"

    # Write the URLs to the file
    with open(output_playlist, 'w') as file:
        for video_url in playlist.video_urls:
            file.write(video_url + "\n")

    # Path to the file containing the URLs
    file_path = "urls.txt"

    # Output folder for the videos
    output_file = input_file

    # Read URLs from the file
    url_list = read_urls_from_file(file_path)

    # Call the function to download the videos, saving them to the 'output_file' folder
    if url_list:
        download_videos(url_list, output_folder=output_file)
        
    else:
        print("No URLs found in the file.")

    again = str(input('again? [s/n]: '))

    if again.lower() == 'n' or again.strip() == '':
        break
    
    os.system('cls')
