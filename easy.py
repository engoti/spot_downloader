import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp
import json

class SpotifyPlaylistDownloader:
    def __init__(self, client_id, client_secret):
        """
        Initialize Spotify client with credentials
        
        :param client_id: Spotify Developer Client ID
        :param client_secret: Spotify Developer Client Secret
        """
        self.client_credentials_manager = SpotifyClientCredentials(
            client_id=client_id, 
            client_secret=client_secret
        )
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)

    def get_playlist_tracks(self, playlist_id):
        """
        Retrieve all tracks from a Spotify playlist
        
        :param playlist_id: Spotify Playlist ID
        :return: List of track details
        """
        results = self.sp.playlist_tracks(playlist_id)
        tracks = results['items']
        
        while results['next']:
            results = self.sp.next(results)
            tracks.extend(results['items'])
        
        return tracks

    def format_track_name(self, track):
        """
        Create a formatted search query for YouTube
        
        :param track: Spotify track object
        :return: Formatted track search string
        """
        artists = ' '.join([artist['name'] for artist in track['track']['artists']])
        return f"{track['track']['name']} {artists}"

    def download_track(self, track_name, output_path):
        """
        Download a track from YouTube with 320 kbps quality
        
        :param track_name: Search query for track
        :param output_path: Directory to save downloaded track
        :return: Path to downloaded file or None
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'nooverwrites': True,
            'no_color': True,
            'quiet': False,
            'no_warnings': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(f"ytsearch:{track_name}", download=True)
                if 'entries' in info:
                    # Get the first downloaded file
                    for download in info.get('entries', []):
                        if 'requested_downloads' in download:
                            return download['requested_downloads'][0]['filepath']
            except Exception as e:
                print(f"Error downloading {track_name}: {e}")
                return None

    def download_playlist(self, playlist_id, output_directory=None):
        """
        Download entire Spotify playlist
        
        :param playlist_id: Spotify Playlist ID
        :param output_directory: Directory to save downloaded tracks
        """
        # If no output directory specified, use Downloads folder
        if output_directory is None:
            output_directory = os.path.join(os.path.expanduser('~'), 'Downloads', 'SpotifyDownloads')
        
        # Create output directory if it doesn't exist
        os.makedirs(output_directory, exist_ok=True)
        
        # Get playlist tracks
        tracks = self.get_playlist_tracks(playlist_id)
        
        # Download each track
        downloaded_tracks = []
        for track in tracks:
            track_name = self.format_track_name(track)
            print(f"Downloading: {track_name}")
            
            downloaded_file = self.download_track(track_name, output_directory)
            
            if downloaded_file:
                downloaded_tracks.append({
                    'original_name': track_name,
                    'file_path': downloaded_file
                })
        
        # Save download log
        with open(os.path.join(output_directory, 'download_log.json'), 'w') as f:
            json.dump(downloaded_tracks, f, indent=2)
        
        print(f"Downloaded {len(downloaded_tracks)} tracks to {output_directory}")
        print("A download log has been saved in the same directory.")

def main():
    # Replace with your Spotify Developer credentials
    CLIENT_ID = 'your_spotify_client_id'
    CLIENT_SECRET = 'your_spotify_client_secret'
    
    # Replace with your Spotify Playlist ID
    PLAYLIST_ID = 'spotify:playlist:your_playlist_id'
    
    downloader = SpotifyPlaylistDownloader(CLIENT_ID, CLIENT_SECRET)
    downloader.download_playlist(PLAYLIST_ID)

if __name__ == "__main__":
    main()