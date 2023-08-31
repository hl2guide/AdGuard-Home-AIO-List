"""Creates a consolidated blocklist for many source files."""

# Downloads blocklists, combines them to one list,
# removes comment lines, sorts all lines and then makes lines unique

from urllib.request import urlretrieve

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
        #"https://hosts.anudeep.me/mirror/adservers.txt",
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

for URL in URLS:
    LIST_INDEX = URLS.index(URL)
    FILENAME = "downloaded_lists/blocklist" + str(LIST_INDEX) + ".txt"
    urlretrieve(URL, FILENAME)
    print("Downloading: "+ FILENAME)
