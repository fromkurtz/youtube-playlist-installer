# YouTube Playlist Downloader
This script downloads all videos from a YouTube playlist or a list of YouTube video URLs and saves them in MP4 format to a specified folder. It uses the ```pytube``` library and provides an interactive interface for users to specify the playlist URL and output folder.

## Features
- Reads video URLs from a YouTube playlist or a text file.
- Downloads YouTube videos in the highest resolution available (MP4 format).
- Allows users to specify the output folder for saving the downloaded videos.
- Provides an option to run the script multiple times without restarting.

## Prerequisites
1. **Python**: Ensure Python is installed (version 3.6 or later is recommended).
2. **Required Libraries**: Install the following Python libraries:
   - ```pytube```
   - ```pytubefix``` (if necessary for some bug fixes)

To install the required libraries, run: <br/>
```bash
pip install pytube pytubefix
```
## Usage
1. Clone or download the script file.
2. Run the script in a terminal:
   ```bash
   python script_name.py
3. Follow the prompts:
   - Enter the ***URL*** of a YouTube playlist.
   - Specify the folder where videos will be saved.
4. The script will:
   - Extract all video URLs from the playlist.
   - Save these URLs to a file named ```urls.txt.```
   - Download each video in MP4 format to the specified folder.
5.  When prompted, choose whether to repeat the process by entering ```s``` (yes) or ```n ``` (no).
## Example Workflow
1. ***Input Playlist URL***
   ```bash
   URL: https://www.youtube.com/playlist?list=PL123456789
   ```
2. ***Specify Output Folder:***
   ```bash
   my videos will be sent to the folder: C:\Users\YourName\Downloads
   ```
3. ***Output:***
   ```bash
   Downloading: https://www.youtube.com/watch?v=abc123...
    Video 'Example Video 1' downloaded successfully!
    Downloading: https://www.youtube.com/watch?v=xyz456...
    Video 'Example Video 2' downloaded successfully!
4. ***Repeat?:***
5. ```bash
   again [s/n]: n

## Files Created
- ```urls.txt```: A text file containing all video URLs from the playlist.
## Error Handling
- If an error occurs while reading the input file or downloading a video, the script will print an error message and continue with the next video.
## Notes
- Ensure the playlist URL is valid and accessible.
- Verify the output folder exists and has sufficient storage space.
- The script overwrites the urls.txt file during each execution.
## License
This script is provided "as-is" without warranty of any kind. Use it at your own risk and ensure compliance with YouTube's Terms of Service.
