"""Creates a consolidated blocklist for many source files."""

# Downloads blocklists, combines them to one list,
# removes comment lines, sorts all lines and then makes lines unique

from urllib.request import urlretrieve
import glob
import os

URLS = ["https://blocklistproject.github.io/Lists/adguard/crypto-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/drugs-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/fraud-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/malware-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/phishing-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/ransomware-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/scam-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/tracking-ags.txt",
        "https://blocklistproject.github.io/Lists/adguard/abuse-ags.txt"
        # Anudeep's Blacklist
        #"https://hosts.anudeep.me/mirror/adservers.txt",
        # LostAd
        #"https://raw.githubusercontent.com/lennihein/LostAd/main/lostad_dns.txt",
        # ppfeufer / adguard-filter-list
        #"https://raw.githubusercontent.com/ppfeufer/adguard-filter-list/master/blocklist",
        # HaGeZi's Pro DNS Blocklist
        #"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt",
        # HaGeZi's The World's Most Abused TLDs
        #"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds.txt",
        # Steven Black's List
        #"https://adguardteam.github.io/HostlistsRegistry/assets/filter_33.txt",
        # OISD Blockist Big
        #"https://adguardteam.github.io/HostlistsRegistry/assets/filter_27.txt"
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
UNIQUELINES = set(open('aio_blocklist.txt', encoding='utf-8').readlines())
# Sort all lines in the set
UNIQUELINES = sorted(UNIQUELINES)
# Removes duplicates from from text file
CLEANEDOUTPUT = open('aio_blocklist.txt', 'w', encoding='utf-8').writelines(UNIQUELINES)
# Open the file for removing comments
AIOFILE = open('aio_blocklist.txt', encoding='utf-8')
with AIOFILE as file:
    for line in file:
        if line.startswith('#'):
            continue  # skip comments
        line = line.strip()
# Saves the cleaned text file's contents
CLEANEDOUTPUT = open('aio_blocklist.txt', 'w', encoding='utf-8').writelines(UNIQUELINES)
