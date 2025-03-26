# spot_downloader
![image alt](https://github.com/engoti/spot_downloader/blob/7e0b845f96693cfb294f9e5df2e7db580f002581/spot_logo.png)
# Spotify Playlist Downloader

## 📜 Description
This Python script allows you to download songs from a Spotify playlist using YouTube as the source. It provides an easy way to convert your Spotify playlists into downloadable MP3 files.

## 🚀 Features
- Download entire Spotify playlists
- 320 kbps audio quality
- Automatic downloads to Downloads folder
- Detailed download logging
- Easy-to-use interface

## 🛠 Prerequisites
Before you begin, ensure you have the following installed:

### Software Requirements
- Python 3.7 or higher
- FFmpeg
- pip (Python package manager)

### Required Libraries
- spotipy
- yt-dlp
- requests

## 🔧 Installation

### 1. Install Python Libraries
```bash
pip install spotipy yt-dlp requests youtube-search-python
```

### 2. Install FFmpeg
- **Windows**: 
  1. Download from [FFmpeg Official Site](https://ffmpeg.org/download.html)
  2. Add to System PATH

- **macOS** (using Homebrew):
  ```bash
  brew install ffmpeg
  ```

- **Linux**:
  ```bash
  sudo apt-get install ffmpeg
  ```

## 🔐 Spotify Developer Credentials
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create a new application
3. Get your `Client ID` and `Client Secret`

## 🛡 Configuration

### In the Script
Replace the following placeholders in the `main()` function:
```python
CLIENT_ID = 'your_spotify_client_id'
CLIENT_SECRET = 'your_spotify_client_secret'
PLAYLIST_ID = 'spotify:playlist:your_playlist_id'
```

### How to Find Playlist ID
1. Open the playlist in Spotify
2. Click "..." (More Options)
3. Select "Share"
4. Choose "Copy Spotify URI"
5. The URI is your Playlist ID

## 🖥 Usage

### Basic Usage
```bash
python spotify_playlist_downloader.py
```

### Custom Download Location
```python
# In the script, modify the download_playlist call
downloader.download_playlist(PLAYLIST_ID, output_directory='custom/path')
```

## 📂 Output
- Downloads MP3 files to `~/Downloads/SpotifyDownloads/`
- Creates `download_log.json` with download details

## ⚠️ Legal Considerations
- Ensure you have the right to download and use the tracks
- Respect copyright laws
- This script is for personal use only

## 🐛 Troubleshooting
- Verify all credentials are correct
- Check internet connection
- Ensure all libraries are up to date
- Run `pip install --upgrade spotipy yt-dlp`

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License
[Insert Your License Here - e.g., MIT License]

## 🙏 Acknowledgements
- Spotipy Library
- yt-dlp Project
- YouTube
- Spotify

## 📧 Contact
[https://github.com/engoti]
