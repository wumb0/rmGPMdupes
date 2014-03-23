#### Used to remove duplicate songs from google play music playlists ####
#### This is the compatible version ####

from gmusicapi import Mobileclient

def login():
    username = raw_input("Enter your Google Play username: ")
    password = raw_input("Enter your Google Play password: ")
    gpm = Mobileclient()
    if not gpm.login(username, password):
        print("\nNot a valid login")
        exit()
    else:
        print("\nLogin success!")
        return gpm

def main():
    gpm = login()
    for playlist in gpm.get_all_user_playlist_contents():
        isdupes = False
        removed = []
        print(str(playlist['name']))
        for song in playlist['tracks']:
            if not song['id'] in removed:
                numdupes = 0
                dupes = []
                for compsong in playlist['tracks']:
                    if (song['id'] != compsong['id'] and song['trackId'] == compsong['trackId']):
                        isdupes = True
                        numdupes += 1
                        dupes.append(compsong['id'])
                        removed.append(compsong['id'])
                for x in range(0, numdupes):
                    print("Duplicate found! ID: " + str(dupes[x]))
                    gpm.remove_entries_from_playlist(dupes[x]);
        if not (isdupes):
            print("None found")
        print("\n")
main()


