# TikTok OSINT Tool

TikTok Social Media Open Source Intelligence Tool (reloaded from Omicron66's version)

It works under Linux and Windows. Tested with Debian 12 and Windows 11.

![alt text](https://github.com/alcyone6/TikTokOSINT/blob/master/images/image.png?raw=true)

## Requirements

- Python 3
- pip
- git (optional, just for git installation method)
- wget (optional, just for zip method)
- unzip (optional, just for zip method)

## Installation

### Git method
- git clone https://github.com/alcyone6/TikTokOSINT
- cd TikTokOSINT
- pip3 install -r requirements.txt

### Zip method
- wget [https://github.com/alcyone6/TikTokOSINT/archive/refs/heads/master.zip]
- unzip master.zip
- cd TikTokOSINT-master
- pip3 install -r requirements.txt

## Usage

"python3 main.py -u USERNAME -d"

- Replace 'USERNAME' with the username, the @ in the username is optional.
- '-d' tells the tool to download the profile picture. This argument is optional.
If you don't give any args to the app, don't worry, it will ask you again.

## Data

The app gives the user a lot of meta-data about the account if it's public, less if it's private.

1. Profile Name (nickname)
2. Username
3. User Id
4. Region
5. Language
6. Bio
7. Following
8. Followers
9. Like count
10. Video Count
11. Account verification status
12. Private or public
13. Account create date
14. Nickname last modification
