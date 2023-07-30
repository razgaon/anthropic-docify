from dataclasses import dataclass

from typing import Optional
import urllib.parse as urlparse
import logging
from custom_types import Source, SourceType
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build

from env_var import GOOGLE_API_KEY
from src import crawler


logger = logging.getLogger(__name__)

@dataclass
class YoutubeMetadata:
    title: str
    description: str
    channel_title: str
    published_at: str

class YoutubeCrawler(crawler):

    def _get_video_id(self, video_url: str):
        """
        This function extracts the YouTube video ID from an URL.
        """

        url_data = urlparse.urlparse(video_url)
        video_id = urlparse.parse_qs(url_data.query)["v"][0]

        return video_id

    def _get_transcript(self, video_url: str) -> str:
        video_id = self._get_video_id(video_url)
        try:
            # This will return a list of dictionaries, each containing a single part of the transcript
            logger.info("Starting transcribing")
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            logger.info("Finished transcribing")
            # Now we will combine all parts into a single transcript
            transcript = " ".join([d["text"] for d in transcript_list])
            return transcript
        except Exception as e:
            logger.error(f"Error getting transcript for video {video_url}: {e}")
            return ""

    def _get_video_metadata(self, video_url: str) -> Optional[YoutubeMetadata]:
        video_id = self._get_video_id(video_url)

        youtube = build("youtube", "v3", developerKey=GOOGLE_API_KEY)

        request = youtube.videos().list(part="snippet", id=video_id)
        response = request.execute()

        if response["items"]:
            item = response["items"][0]

            title = item["snippet"]["title"]
            description = item["snippet"]["description"]
            channel_title = item["snippet"]["channelTitle"]
            published_at = item["snippet"]["publishedAt"]

            return YoutubeMetadata(
                title=title,
                description=description,
                channel_title=channel_title,
                published_at=published_at,
            )

        else:
            logger.error(f"No metadata found for video: {video_url}")
            return None

    def generate_row(self, url):
        content = self._get_transcript(url)
        authors = []
        metadata = self._get_video_metadata(url)
        if metadata:
            authors.append(metadata.channel_title)
        return Source(
            url=url,
            source_type=SourceType.Youtube,
            content=content,
            authors=authors,
        )
