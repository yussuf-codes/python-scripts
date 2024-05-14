from argparse import ArgumentParser
from re import search, Match
from subprocess import run


HTTP_URL_REGEX_PATTERN: str = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

DOWNLOAD_DIRECTORY: str = r'C:\Users\Joe\Videos\Downloads'
YT_DLP_PATH_OR_COMMAND: str = r'C:\Users\Joe\Documents\Binaries\yt-dlp.exe'


def youtube_video_downloader(url: str):
    VIDEO_PATH: str = DOWNLOAD_DIRECTORY + '/%(title)s.%(ext)s'
    command: list[str] = [YT_DLP_PATH_OR_COMMAND, '-f', '137+bestaudio', '-o', VIDEO_PATH, url]
    run(command)


def main():
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("-l", "--url", type=str)
    args = parser.parse_args()

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
