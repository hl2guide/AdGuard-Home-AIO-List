"""Creates a consolidated blocklist for many source files."""

# Downloads adblocker rules, combines them to one list,
# sorts all lines, makes lines unique, and then removes comment lines

# FOR ADGUARD BROWSER EXTENSION OR A MODERN ADBLOCKER EXTENSION

# Version: 0.1.23

from time import gmtime, strftime
from urllib.request import urlretrieve
import glob
import os

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

URLS = [
        # AdGuard Base Filter
        "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_2_Base/filter.txt",
        # AdGuard URL Tracking filter
        "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_17_TrackParam/filter.txt",
        # AdGuard Tracking Protection filter
        "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_3_Spyware/filter.txt",
        # Fanboy's Enhanced Tracking List
        #"https://secure.fanboy.co.nz/enhancedstats.txt",
        # AdGuard Social media filter
        "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_4_Social/filter.txt",
        # AdGuard Annoyances filter
        "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_14_Annoyances/filter.txt",
        # AdGuard Mobile ads filter
        "https://raw.githubusercontent.com/AdguardTeam/FiltersRegistry/master/filters/filter_11_Mobile/filter.txt",
        # Fanboy's EasyList
        #"https://easylist.to/easylist/easylist.txt",
        # Fanboy's EasyPrivacy
        #"https://easylist.to/easylist/easyprivacy.txt",
        # Fanboy's EasyList Cookie List
        #"https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
        # Fanboy's Annoyance List
        #"https://secure.fanboy.co.nz/fanboy-annoyance.txt",
        # yourduskquibbles webannoyances ultralist
        "https://raw.githubusercontent.com/yourduskquibbles/webannoyances/master/ultralist.txt",
        # I don't care about cookies
        #"https://www.i-dont-care-about-cookies.eu/abp/",
        # Online Malicious URL Blocklist - urlhaus filter
        "https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-ag.txt",
        # NoCoin filter
        "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/nocoin.txt",
        # Scam Blocklist by DurableNapkin
        "https://raw.githubusercontent.com/durablenapkin/scamblocklist/master/adguard.txt",
        # Jarelllama's Scam Blocklist
        "https://raw.githubusercontent.com/jarelllama/Scam-Blocklist/main/lists/adblock/scams.txt"
        ]

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Downloads the individual lists
for URL in URLS:
    LIST_INDEX = URLS.index(URL)
    FILENAME = "downloaded_lists/blocklist" + str(LIST_INDEX) + ".txt"
    print(NOW+" - "+"Downloading: "+ FILENAME)
    urlretrieve(URL, FILENAME)
    NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Merges lists into one file
# Source: https://bobbyhadz.com/blog/merge-text-files-in-python#how-to-merge-text-files-in-python
file_paths = glob.glob('downloaded_lists/*.txt')
with open('adblocker_list.txt', 'w', encoding='utf-8') as output_file:
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            output_file.write(input_file.read() + '\n')

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Removes individual text files
I = 0
while I < len(URLS):
    print(NOW+" - "+"Removing: downloaded_lists/blocklist"+str(I)+".txt")
    os.remove("downloaded_lists/blocklist"+str(I)+".txt")
    I = I + 1

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Cleans adblocker_list.txt file
print(NOW+" - "+"Cleaning adblocker_list.txt, please wait..")
# Open the file
UNIQUELINES = set(open('adblocker_list.txt', 'r', encoding='utf-8').readlines())
# Sort all lines in the set
UNIQUELINES = sorted(UNIQUELINES)
# Removes duplicates from from text file
CLEANEDOUTPUT = open('adblocker_list.txt', 'w', encoding='utf-8').writelines(UNIQUELINES)

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Removes all junk from aio_blocklist.txt file
print(NOW+" - "+"Removing junk lines from adblocker_list.txt, please wait..")
with open("adblocker_list.txt", "r", encoding='utf-8') as f:
    LINES = f.readlines()
with open("adblocker_list_final.txt", "w", encoding='utf-8') as new_f:
    for line in LINES:
        if not line.startswith("!") and not line.startswith("#") and not line.startswith("["):
            new_f.write(line)
os.remove("adblocker_list.txt")

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(NOW+" - "+"Adblocker AIO list has been generated as: adblocker_list_final.txt")

# Write to HISTORY.md file
#with open("HISTORY.md", "a", encoding='utf-8') as HISTORYFILE:
#    HISTORYFILE.write("- Updated "+NOW+"\n")
