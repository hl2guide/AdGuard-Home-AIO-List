"""Creates a consolidated blocklist for many source files."""

# Downloads blocklists, combines them to one list,
# sorts all lines, makes lines unique, and then removes comment lines

# The final AIO list is: aio_blocklist_final.txt

# FOR ADGUARD HOME ONLY

# Required Packages
# A python package called "requests" is required to handle 403 errors (install that package first by running: python -m pip install requests)

# Version: 0.2
# Date: 2024-06-14 01:20:58AM

# Imports
from time import gmtime, strftime
from urllib.request import urlretrieve
import requests
#from urllib.request import Request, urlopen
#import requests
#from random import seed
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
        # ph00lt0 / blocklist : https://github.com/ph00lt0/blocklist
        "https://raw.githubusercontent.com/ph00lt0/blocklists/master/blocklist.txt",
        # Deanoman - tracker_list_adguard_home
        "https://raw.githubusercontent.com/hl2guide/AdGuard-Home-AIO-List/main/tracker_list_adguard_home.txt",
        # blocklistproject ads-ags.txt : https://github.com/blocklistproject/Lists
        "https://blocklistproject.github.io/Lists/adguard/ads-ags.txt",
        # blocklistproject crypto-ags.txt : https://github.com/blocklistproject/Lists
        "https://blocklistproject.github.io/Lists/adguard/crypto-ags.txt",
        # blocklistproject drugs-ags.txt : https://github.com/blocklistproject/Lists
        "https://blocklistproject.github.io/Lists/adguard/drugs-ags.txt",
        # blocklistproject fraud-ags.txt : https://github.com/blocklistproject/Lists
        "https://blocklistproject.github.io/Lists/adguard/fraud-ags.txt",
        # blocklistproject phishing-ags.txt : https://github.com/blocklistproject/Lists
        "https://blocklistproject.github.io/Lists/adguard/phishing-ags.txt",
        # blocklistproject ransomware-ags.txt : https://github.com/blocklistproject/Lists
        "https://blocklistproject.github.io/Lists/adguard/ransomware-ags.txt",
        # blocklistproject scam-ags.txt : https://github.com/blocklistproject/Lists
        "https://blocklistproject.github.io/Lists/adguard/scam-ags.txt",
        # blocklistproject tracking-ags.txt : https://github.com/blocklistproject/Lists
        "https://blocklistproject.github.io/Lists/adguard/tracking-ags.txt",
        # Multi PRO - Extended protection : https://github.com/hagezi/dns-blocklists
        "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt",
        # Anudeep's Blacklist : https://github.com/anudeepND/blacklist
        "https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt",
        # romainmarcoux / malicious-ip : https://github.com/romainmarcoux/malicious-ip
        "https://raw.githubusercontent.com/romainmarcoux/malicious-ip/main/full-40k.txt",
        # borestad / blocklist-abuseipdb : https://github.com/borestad/blocklist-abuseipdb
        "https://raw.githubusercontent.com/borestad/blocklist-abuseipdb/main/abuseipdb-s100-60d.ipv4",
        # ipsum : https://github.com/stamparm/ipsum
        "https://raw.githubusercontent.com/stamparm/ipsum/master/levels/3.txt",
        # Sefinek-Blocklist-Collection (many lists) - https://sefinek.net/blocklist-generator/adguard
        "https://blocklist.sefinek.net/generated/v1/adguard/abuse/blocklistproject/hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/abuse/urlhaus.abuse.ch/hostfile.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/0Zinc/easylist.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/DandelionSprout.GameConsoleAdblockList.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/FadeMind/UncheckyAds.fork.txt",
        #"https://blocklist.sefinek.net/generated/v1/adguard/ads/MajkiIT/SmartTV-ads.fork.txt", # Testing Samsung TV login issues 05.06.2024
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/ShadowWhisperer/Ads.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/adaway/hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/anudeepND/adservers.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/blocklistproject/hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/blocklistproject/youtube.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/craiu/mobiletrackers.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/crazy-max/spy.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/disconnectme/simple-ad.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/firebog/AdguardDNS.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/firebog/Admiral.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/firebog/Easylist.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/firebog/Prigent-Ads.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/jerryn70/GoodbyeAds.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/r-a-y/AdguardMobileAds.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/sefinek.hosts.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ads/yoyo/ads-trackers-etc.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/amp/developerdan/amp-hosts-extended.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/amp/ente-dev/google-amp-hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/anime/myanimelist.net.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/anime/shinden.pl.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/apps/whatsapp.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/crypto/cryptojacking/Snota418/Crypto-streams.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/crypto/cryptojacking/firebog/Prigent/Crypto.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/crypto/cryptojacking/hoshsadiq/adblock-nocoin-list.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/crypto/cryptojacking/zerodot1/CoinBlockerLists-hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/crypto/sites/sefinek.hosts.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/dating-services/developerdan/extended.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/dead-domains/jarelllama/dead-domains.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/drugs/blocklistproject/drugs.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/FadeMind/add-2o7Net.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/MajkiIT/adguard-host.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/MajkiIT/easy-privacy-host.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/cbuijs/adult-domains-24733.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/deathbybandaid/CountryCodesLists-France.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/deathbybandaid/ParsedBlacklists-EasyList-Liste-FR.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/deathbybandaid/ParsedBlacklists-EasyList.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/hagezi/pro.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/justdomains/adguarddns-justdomains.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/oisd/big.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/r-a-y/AdguardApps.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/extensions/r-a-y/AdguardMobileSpyware.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/fakenews/StevenBlack/hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/fakenews/marktron/hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/fraud/blocklistproject/hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/gambling/MajkiIT/gambling-hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/gambling/StevenBlack/hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/gambling/TrustPositif/gambling-indonesia.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/gambling/blocklistproject/hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/gambling/sefinek.hosts.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/games/league-of-legends.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/games/valorant.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/hate-and-junk/developerdan/extended.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/AssoEchap/stalkerware-indicators.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/DandelionSprout-AntiMalwareHosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/RPiList/Malware.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/Spam404/main-blacklist.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/bigdargon/hostsVN.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/blocklistproject/malware.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/digitalside/latestdomains.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/disconnectme/simple-malvertising.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/malware-filter/urlhaus-filter-hosts-online.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/phishing.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/quidsup/notrack-malware.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/reported-by-norton.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/sefinek.hosts1.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/sefinek.hosts2.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/suspicious.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/malicious/web-attacks.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/phishing/Dogino/Discord-Phishing-URLs-phishing.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/phishing/RPiList/Phishing-Angriffe.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/phishing/blocklistproject/phishing.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/phishing/phishing.army/blocklist-extended.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/porn/4skinSkywalker/hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/porn/Sinfonietta/pornography-hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/porn/StevenBlack/porn.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/porn/blocklistproject/porn.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/porn/chadmayfield/pi-blocklist-porn-all.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/porn/oisd/nsfw.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/porn/sefinek.hosts.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/ransomware/blocklistproject/ransomware.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/redirect/blocklistproject/redirect.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/scam/Dogino/Discord-Phishing-URLs-scam.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/scam/blocklistproject/scam.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/scam/durablenapkin/scamblocklist.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/scam/jarelllama/scam.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/sites/booth.pm.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/sites/gamebanana.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/sites/omegle.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/sites/patreon.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/sites/pinterest.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/sites/pixiv.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/sites/riotgames.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/social/facebook.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/social/instagram.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/social/snapchat.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/social/tiktok.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/social/twitter.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/spam/FadeMind/add-Spam.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/spam/RPiList/spam-mails.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/spam/stopforumspam/toxic-domains-whole.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/suspicious/FadeMind/add-Risk.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/suspicious/firebog/w3kbl.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/test.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/tracking-and-telemetry/0Zinc/easyprivacy.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/tracking-and-telemetry/MajkiIT/adguard-mobile-host.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/tracking-and-telemetry/ente-dev/tv.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/tracking-and-telemetry/frogeye/firstparty-trackers-hosts.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/tracking-and-telemetry/mitchellkrogza/INACTIVE.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/tracking-and-telemetry/neodevpro/host.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/tracking-and-telemetry/quidsup/trackers-hosts.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/useless-websites/jarelllama/parked-domains.fork.txt",
        "https://blocklist.sefinek.net/generated/v1/adguard/useless-websites/sefinek.hosts.txt",

        #"https://hosts.anudeep.me/mirror/adservers.txt"
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
#    print(NOW+" - "+"Downloading: " + URL + "  >>  " + FILENAME)
#    urlretrieve(URL, FILENAME)
#    NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    # Uses a workaround for 403 errors by applying a better "User-Agent" header to the request
    if URL.startswith("https://blocklist.sefinek.net/"):
        print(NOW+" - "+"Downloading: " + URL + "  >>  " + FILENAME)
        HEADERS = {
            'User-Agent': 'Mozilla 5.0',
        }
        RESPONSE = requests.get(URL, headers=HEADERS)
        CONTENT = RESPONSE.text
        if RESPONSE.status_code == 200:
            with open(FILENAME, "w", encoding='utf8') as file:
                file.write(CONTENT)
        NOW = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    else:
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
        and not line.startswith("$removeparam=") and not line.startswith("*") \
        and not line.startswith("-") and not line.startswith(".") and not line.startswith("/"):
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
            if not (line == '') and not (line == ' ') and not (line == '||') and not (line == '##'):
                line = line.replace('^','^$important')
                line = line.replace('||||','||')
                line = line.replace('|||','||')
                line = line.replace('$important$important','$important')
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
