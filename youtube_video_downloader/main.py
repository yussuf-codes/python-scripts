import subprocess


if __name__ == '__main__':
    YT_DLP_PATH_OR_COMMAND = 'C:\\Users\\Joe\\Documents\\Binaries\\yt-dlp.exe'
    DOWNLOAD_DIRECTORY = 'C:\\Users\\Joe\\Videos\\Downloads'
    VIDEO_PATH = DOWNLOAD_DIRECTORY + '/%(title)s.%(ext)s'
    URL = 'https://www.youtube.com/watch?v=i_yLpCLMaKk'
    command = [YT_DLP_PATH_OR_COMMAND, '-f', '22', '-o', VIDEO_PATH, URL]
    subprocess.run(command)
