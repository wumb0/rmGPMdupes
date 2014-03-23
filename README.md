GPMdupes
==========

Removing duplicate songs in google play music got really annoying to do manually... so I wrote this.

There is a compatible branch that displays your password on the screen, the master branch is for nix only because it uses system calls to suppress output on the terminal (stty -echo and stty echo) for password entry. 

If you are on windows use the compatible branch :)

If you have problems with the master branch on your nix system use the compatible branch.

Usage
----------
Install pip
```
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py
```

Install gmusicapi
```
sudo pip install gmusicapi
```

Run rmGPMdupes.py
```
./rmGPMdupes.py
```

That's it!

Enjoy!
