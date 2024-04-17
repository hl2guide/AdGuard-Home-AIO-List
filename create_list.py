"""Creates a consolidated blocklist for many source files."""

# Downloads blocklists, combines them to one list,
# sorts all lines, makes lines unique, and then removes comment lines

# The final AIO list is: aio_blocklist_final.txt

# FOR ADGUARD HOME ONLY

# Version: 0.1.24
# Date: 16th of April, 2024

# Imports
from time import gmtime, strftime
from urllib.request import urlretrieve
import glob
import os

#CURRENTWORKINGDIRECTORY = os.getcwd() + "\\"
CURRENTWORKINGDIRECTORY = "C:\\Users\\Dean\\Documents\\Important\\MEGASync\\GitHub\\CodeLibrary\\Python\\AdGuard-Home-AIO-List-main\\"

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

URLS = [
        # AdGuard Simplified Domain Names filter
        "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt",
        # 🔮 Most Abused TLDs
        "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds.txt",
        # 1Hosts (Lite)
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_24.txt",
        # AdGuard DNS filter
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt",
        # OISD Blocklist Small
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_5.txt",
        # Phishing URL Blocklist (PhishTank and OpenPhish)
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_30.txt",
        # Scam Blocklist by DurableNapkin
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_10.txt",
        # The Big List of Hacked Malware Web Sites
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_9.txt",
        # Malicious URL Blocklist (URLHaus)
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_11.txt",
        # Phishing Army
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_18.txt",
        # ShadowWhisperer's Malware List
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_42.txt",
        # Stalkerware Indicators List
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_31.txt",
        # uBlock₀ filters - Badware risks
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_50.txt",
        # Steven Black's List
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_33.txt",
        # Peter Lowe's Blocklist
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_3.txt",
        # Dandelion Sprout's Anti Push Notifications
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_39.txt",
        # AdAway Default Blocklist
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_2.txt",
        # Dan Pollock's List
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt",
        # WindowsSpyBlocker - Hosts spy rules
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_23.txt",
        # Dandelion Sprout's Anti-Malware List
        "https://adguardteam.github.io/HostlistsRegistry/assets/filter_12.txt",
        # ph00lt0 / blocklist
        "https://raw.githubusercontent.com/ph00lt0/blocklists/master/blocklist.txt",
        # Deanoman - tracker_list_adguard_home
        "https://raw.githubusercontent.com/hl2guide/AdGuard-Home-AIO-List/main/tracker_list_adguard_home.txt",
        # blocklistproject ads-ags.txt
        "https://blocklistproject.github.io/Lists/adguard/ads-ags.txt",
        # blocklistproject crypto-ags.txt
        "https://blocklistproject.github.io/Lists/adguard/crypto-ags.txt",
        # blocklistproject drugs-ags.txt
        "https://blocklistproject.github.io/Lists/adguard/drugs-ags.txt",
        # blocklistproject fraud-ags.txt
        "https://blocklistproject.github.io/Lists/adguard/fraud-ags.txt",
        # blocklistproject phishing-ags.txt
        "https://blocklistproject.github.io/Lists/adguard/phishing-ags.txt",
        # blocklistproject ransomware-ags.txt
        "https://blocklistproject.github.io/Lists/adguard/ransomware-ags.txt",
        # blocklistproject scam-ags.txt
        "https://blocklistproject.github.io/Lists/adguard/scam-ags.txt",
        # blocklistproject tracking-ags.txt
        "https://blocklistproject.github.io/Lists/adguard/tracking-ags.txt",
        # Multi PRO - Extended protection
        "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt",
        # Anudeep's Blacklist
        "https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt",
        # LostAd [TOO BIG]
        #"https://raw.githubusercontent.com/lennihein/LostAd/main/lostad_dns.txt",
        # ppfeufer / adguard-filter-list [TOO BIG]
        #"https://raw.githubusercontent.com/ppfeufer/adguard-filter-list/master/blocklist",
        # HaGeZi's Pro DNS Blocklist [TOO BIG]
        #"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt",
        # HaGeZi's The World's Most Abused TLDs
        #"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds.txt",
        # HaGeZi's Gambling DNS Blocklist [TOO BIG]
        #"https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/gambling.txt",
        # Steven Black's List [INCLUDED ALREADY]
        #"https://adguardteam.github.io/HostlistsRegistry/assets/filter_33.txt",
        # OISD Blockist Big
        #"https://adguardteam.github.io/HostlistsRegistry/assets/filter_27.txt",
        # AdGuard Simplified Domain Names filter
        #"https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"
        ]

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Downloads the individual lists
for URL in URLS:
    LIST_INDEX = URLS.index(URL)
    FILENAME = CURRENTWORKINGDIRECTORY + "downloaded_lists\\blocklist" + str(LIST_INDEX) + ".txt"
    print(NOW+" - "+"Downloading: " + URL + "  >>  " + FILENAME)
    urlretrieve(URL, FILENAME)
    NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Merges lists into one file
# Source: https://bobbyhadz.com/blog/merge-text-files-in-python#how-to-merge-text-files-in-python
file_paths = glob.glob(CURRENTWORKINGDIRECTORY + 'downloaded_lists/*.txt')
with open(CURRENTWORKINGDIRECTORY + 'aio_blocklist.txt', 'w', encoding='utf-8') as output_file:
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            output_file.write(input_file.read() + '\n')

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Removes individual text files
I = 0
while I < len(URLS):
    print(NOW+" - "+"Removing: downloaded_lists/blocklist"+str(I)+".txt")
    os.remove(CURRENTWORKINGDIRECTORY + "downloaded_lists/blocklist"+str(I)+".txt")
    I = I + 1

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Cleans aio_blocklist.txt file
print(NOW+" - "+"Cleaning aio_blocklist.txt, please wait..")
# Open the file
UNIQUELINES = set(open(CURRENTWORKINGDIRECTORY + 'aio_blocklist.txt', 'r', encoding='utf-8').readlines())
# Sort all lines in the set
UNIQUELINES = sorted(UNIQUELINES)
# Removes duplicates from from text file
CLEANEDOUTPUT = open(CURRENTWORKINGDIRECTORY + 'aio_blocklist.txt', 'w', encoding='utf-8').writelines(UNIQUELINES)

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Removes all junk from aio_blocklist.txt file
print(NOW+" - "+"Removing junk lines from aio_blocklist.txt, please wait..")
with open(CURRENTWORKINGDIRECTORY + "aio_blocklist.txt", "r", encoding='utf-8') as f:
    LINES = f.readlines()
with open(CURRENTWORKINGDIRECTORY + "aio_blocklist_final.txt", "w", encoding='utf-8') as new_f:
    for line in LINES:
        if not line.startswith("!") and not line.startswith("#") and not line.startswith("@@") \
        and not line.startswith("$removeparam="):
            # Removes line prefixes
            line = line.replace('0.0.0.0 ','')
            line = line.replace('127.0.0.1 ','')
            if line.endswith('^'):
                line = line.replace('^','^$important')
            if not line.startswith("/") and not line.startswith("||") and not line.startswith("*") \
            and not line.startswith("-") and not line.startswith("."):
                line = '||' + line
                line = line.replace('||||','||')
                line = line.replace('^','^$important')
            if not (line == '') and not (line == ' ') and not (line == '||') and not '##' in line:
                line = line.replace('^','^$important')
                new_f.write(line)
os.remove(CURRENTWORKINGDIRECTORY + "aio_blocklist.txt")

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Cleans aio_blocklist_final.txt file
print(NOW+" - "+"Cleaning aio_blocklist_final.txt, please wait..")
# Open the file
UNIQUELINES = set(open(CURRENTWORKINGDIRECTORY + 'aio_blocklist_final.txt', 'r', encoding='utf-8').readlines())
# Sort all lines in the set
UNIQUELINES = sorted(UNIQUELINES)
# Remove invalid line = ||
#UNIQUELINES.remove("\|\|")
# Removes duplicates from from text file
CLEANEDOUTPUT = open(CURRENTWORKINGDIRECTORY + 'aio_blocklist_final.txt', 'w', encoding='utf-8').writelines(UNIQUELINES)

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(NOW+" - "+"AIO list has been generated as: aio_blocklist_final.txt")

# Writes to HISTORY.md file
with open(CURRENTWORKINGDIRECTORY + "HISTORY.md", "a", encoding='utf-8') as HISTORYFILE:
    HISTORYFILE.write("- Updated "+NOW+"\n")

NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(NOW+" - "+"Updated: HISTORY.md")
