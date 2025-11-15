
import requests
from bs4 import BeautifulSoup
import json

def scrape_youtube_playlist(playlist_url):
    """
    Scrapes a YouTube playlist page for video titles and URLs.

    Args:
        playlist_url: The URL of the YouTube playlist.

    Returns:
        A list of dictionaries, where each dictionary contains the 'title' and 'url' of a video.
    """
    try:
        response = requests.get(playlist_url)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the playlist URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    videos = []
    for a_tag in soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-playlist-video-renderer'}):
        if 'href' in a_tag.attrs:
            video_url = 'https://www.youtube.com' + a_tag['href']
            video_title = a_tag.find('span', {'id': 'video-title'})
            if video_title:
                videos.append({'title': video_title.text.strip(), 'url': video_url})

    return videos

if __name__ == '__main__':
    # Replace with the URL of the "Watch Later" playlist you want to scrape
    # Note: You will need to make your "Watch Later" playlist public for this to work.
    # To do this, go to your playlist page, click the three dots, go to "Playlist settings", and set the privacy to "Public".
    playlist_url = 'YOUR_PLAYLIST_URL'

    if playlist_url == 'YOUR_PLAYLIST_URL':
        print("Please replace 'YOUR_PLAYLIST_URL' with the actual URL of your YouTube playlist.")
    else:
        video_list = scrape_youtube_playlist(playlist_url)

        if video_list:
            print(json.dumps(video_list, indent=2))
        else:
            print("No videos found or an error occurred.")
