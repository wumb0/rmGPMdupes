#!/usr/bin/env python

""" Used to remove duplicate songs from google play music playlists """

from gmusicapi import Mobileclient
from getpass import getpass

def login():
    username = raw_input("Enter your Google Play username: ")
    password = getpass("Enter your Google Play password: ")
    gpm = Mobileclient()
    if not gpm.login(username, password, "null"):
        print("\nNot a valid login")
        exit()
    else:
        print("\nLogin success!")
        return gpm

def main():
    gpm = login()
    for playlist in gpm.get_all_user_playlist_contents():
        dupes = []
        try:
            print(str(playlist['name']))
        except:
            print("Can't print the name... :(")
        for song in playlist['tracks']:
            if not song['id'] in dupes:
                for compsong in playlist['tracks']:
                    if (song['id'] != compsong['id'] and song['trackId'] == compsong['trackId']):
                        dupes.append(compsong['id'])
        if dupes:
            print("Found {} duplicates! Removing... ".format(len(dupes)))
            gpm.remove_entries_from_playlist(dupes)
        else:
            print("None found")

if __name__ == '__main__':
    main()
