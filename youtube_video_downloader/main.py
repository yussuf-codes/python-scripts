import subprocess


def youtube_video_downloader(url: str):
    YT_DLP_PATH_OR_COMMAND = 'C:\\Users\\Joe\\Documents\\Binaries\\yt-dlp.exe'
    DOWNLOAD_DIRECTORY = 'C:\\Users\\Joe\\Videos\\Downloads'
    VIDEO_PATH = DOWNLOAD_DIRECTORY + '/%(title)s.%(ext)s'
    command = [YT_DLP_PATH_OR_COMMAND, '-f', '137+bestaudio', '-o', VIDEO_PATH, url]
    subprocess.run(command)


if __name__ == '__main__':
    youtube_video_downloader('https://www.youtube.com/watch?v=FZR0rG3HKIk')
