"""Creates a consolidated blocklist for many source files."""

# Downloads blocklists, combines them to one list,
# sorts all lines, makes lines unique, and then removes comment lines

from urllib.request import urlretrieve
import glob
import os
from time import gmtime, strftime

URLS = ["https://blocklistproject.github.io/Lists/adguard/crypto-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/drugs-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/fraud-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/malware-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/phishing-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/ransomware-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/scam-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/tracking-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/abuse-ags.txt",
        # Anudeep's Blacklist
        "https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt",
        # LostAd
        "https://raw.githubusercontent.com/lennihein/LostAd/main/lostad_dns.txt",
        # ppfeufer / adguard-filter-list
        "https://raw.githubusercontent.com/ppfeufer/adguard-filter-list/master/blocklist",
        # HaGeZi's Pro DNS Blocklist
        "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt",
        # HaGeZi's The World's Most Abused TLDs
        "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds.txt",
        # Steven Black's List
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_33.txt",
        # OISD Blockist Big
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_27.txt"
        ]

# Downloads the individual lists
for URL in URLS:
    LIST_INDEX = URLS.index(URL)
    FILENAME = "downloaded_lists/blocklist" + str(LIST_INDEX) + ".txt"
    print("Downloading: "+ FILENAME)
    urlretrieve(URL, FILENAME)

# Merges lists into one file
# Source: https://bobbyhadz.com/blog/merge-text-files-in-python#how-to-merge-text-files-in-python
file_paths = glob.glob('downloaded_lists/*.txt')
with open('aio_blocklist.txt', 'w', encoding='utf-8') as output_file:
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            output_file.write(input_file.read() + '\n')

# Removes individual text files
I = 0
while I < len(URLS):
    print("Removing: downloaded_lists/blocklist"+str(I)+".txt")
    os.remove("downloaded_lists/blocklist"+str(I)+".txt")
    I = I + 1

# Cleans aio_blocklist.txt file
print("Cleaning aio_blocklist.txt, please wait..")
# Open the file
UNIQUELINES = set(open('aio_blocklist.txt', 'r', encoding='utf-8').readlines())
# Sort all lines in the set
UNIQUELINES = sorted(UNIQUELINES)
# Removes duplicates from from text file
CLEANEDOUTPUT = open('aio_blocklist.txt', 'w', encoding='utf-8').writelines(UNIQUELINES)

# Removes all junk from aio_blocklist.txt file
print("Removing junk lines from aio_blocklist.txt, please wait..")
with open("aio_blocklist.txt", "r", encoding='utf-8') as f:
    LINES = f.readlines()
with open("aio_blocklist_final.txt", "w", encoding='utf-8') as new_f:
    for line in LINES:
        if not line.startswith("!") or line.startswith("#") or line.startswith("@@"):
            new_f.write(line)
os.remove("aio_blocklist.txt")
print("AIO list has been generated.")

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())
