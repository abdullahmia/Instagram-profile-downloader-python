import instaloader
import os
import platform
import time


operating_system = platform.system()


def clear_screen():
    if operating_system == 'Windows':
        os.system('cls')
    elif operating_system == 'Linux':
        os.system('clear')

def imgDownload():
    clear_screen()
    cli_header = '''
        Instagram Profile Downloader
        ============================
    '''
    print(cli_header)
    ig = instaloader.Instaloader()
    profile = input('Enter Username: ')
    try:
        ig.download_profile(profile, profile_pic_only=True)
        print('Download Successful')
    except Exception as e:
        print()
        print("Invalid Username........")
        time.sleep(3)
        clear_screen()
        return imgDownload()


def run():
    while True:
        imgDownload()
        user_command = input("Do you want to continue(y/n): ")
        if user_command.lower() == 'y':
            continue
        elif user_command.lower() == 'n':
            print('Thanks For Use')
            break
        else:
            print("Ok Bye.")
            break


if __name__ == '__main__':
    run()
