from argparse import ArgumentParser, Namespace
from re import search, Match
from subprocess import run
from os import environ

UNIX_HOME_DIRECTORY = environ['HOME']

HTTP_URL_REGEX_PATTERN: str = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

DOWNLOAD_DIRECTORY: str = fr'{UNIX_HOME_DIRECTORY}/Videos'
YT_DLP_PATH_OR_COMMAND: str = fr'{UNIX_HOME_DIRECTORY}/bin/yt-dlp'

QUALITY: str = '137+bestaudio'


def youtube_video_downloader(url: str) -> None:
    VIDEO_PATH: str = DOWNLOAD_DIRECTORY + '/%(title)s.%(ext)s'
    command: list[str] = [YT_DLP_PATH_OR_COMMAND, '-f', QUALITY, '-o', VIDEO_PATH, url]
    run(command)


def main() -> None:
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("-l", "--url", type=str)
    args: Namespace = parser.parse_args()

    url_arg: str | None = args.url

    if url_arg is None:
        raise ValueError('URL is not provided')

    url_match_obj: Match[str] | None = search(HTTP_URL_REGEX_PATTERN, url_arg)

    if url_match_obj is None:
        raise ValueError('Invalid URL')

    url: str = url_match_obj.string

    youtube_video_downloader(url)


if __name__ == '__main__':
    main()
