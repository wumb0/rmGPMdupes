#!/usr/bin/env python

#### Used to remove duplicate songs from google play music playlists ####
#### Only works on *Nix systems ####

from gmusicapi import Mobileclient
from getpass import getpass
from sys import argv

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
        isdupes = False
        removed = []
        try:
            print(str(playlist['name']))
        except:
            print("Can't print the name... :(")
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

if __name__ == '__main__':
    main()


