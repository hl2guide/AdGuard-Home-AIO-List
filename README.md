# AdGuard-Home-AIO-List

An All-In-One AdGuard Home blocklist and allowlist.

Version: 0.1.24 (Beta 4)

Updated (AEST): 2024-04-17 03:23:56PM

## Repo Status

- Written in **Python** it now has been updated for 2024 and have new lists added
- I attempted and tested using **GitHub Codespaces** and **github LFS** but moved away from both due to filesize restrictions
- **BETA version 4** is now available for testing, please report all issues here on GitHub
- Currently around **1.1 million unique rules** are included
- The blocklist will make AdGuard Home's RAM usage increase to around **229MB**
- Do not use these lists on older hardware with fewer than **4 CPU cores** or **IOT** devices
- Be prepared to make your own whitelist additions within AdGuard Home, depending on your needs

## Included Blocklists

- [1Hosts (Lite)](https://adguardteam.github.io/HostlistsRegistry/assets/filter_24.txt)
- [AdGuard DNS filter](https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt)
- [AdGuard Simplified Domain Names filter](https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt) by AdGuard
- [Anudeep's Blacklist](https://github.com/anudeepND/blacklist) - [RAW](https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt) by Anudeep
- [Blocklist Project](https://github.com/blocklistproject/Lists)
    - [Abuse](https://blocklistproject.github.io/Lists/adguard/abuse-ags.txt)
    - [Crypto](https://blocklistproject.github.io/Lists/adguard/crypto-ags.txt)
    - [Drugs](https://blocklistproject.github.io/Lists/adguard/drugs-ags.txt)
    - [Fraud](https://blocklistproject.github.io/Lists/adguard/fraud-ags.txt)
    - [Malware](https://blocklistproject.github.io/Lists/adguard/malware-ags.txt)
    - [Phishing](https://blocklistproject.github.io/Lists/adguard/phishing-ags.txt)
    - [Ransom](https://blocklistproject.github.io/Lists/adguard/ransomware-ags.txt)
    - [Scam](https://blocklistproject.github.io/Lists/adguard/scam-ags.txt)
    - [Tracking](https://blocklistproject.github.io/Lists/adguard/tracking-ags.txt)
- [AdAway Default Blocklist](https://adguardteam.github.io/HostlistsRegistry/assets/filter_2.txt)
- [Dan Pollock's List](https://adguardteam.github.io/HostlistsRegistry/assets/filter_4.txt)
- [Dandelion Sprout's Anti Push Notifications](https://adguardteam.github.io/HostlistsRegistry/assets/filter_39.txt)
- [Dandelion Sprout's Anti-Malware List](https://adguardteam.github.io/HostlistsRegistry/assets/filter_12.txt)
- [Deanoman - tracker_list_adguard_home](https://raw.githubusercontent.com/hl2guide/AdGuard-Home-AIO-List/main/tracker_list_adguard_home.txt)
- [HaGeZi's The World's Most Abused TLDs](https://github.com/hagezi/dns-blocklists) - [RAW](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/spam-tlds.txt) by HaGeZi
- [Malicious URL Blocklist (URLHaus)](https://adguardteam.github.io/HostlistsRegistry/assets/filter_11.txt)
- [Multi PRO - Extended protection](https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt)
- [OISD Blocklist Small](https://adguardteam.github.io/HostlistsRegistry/assets/filter_5.txt)
- [Peter Lowe's Blocklist](https://adguardteam.github.io/HostlistsRegistry/assets/filter_3.txt)
- [Phishing Army](https://adguardteam.github.io/HostlistsRegistry/assets/filter_18.txt)
- [Phishing URL Blocklist (PhishTank and OpenPhish)](https://adguardteam.github.io/HostlistsRegistry/assets/filter_30.txt)
- [ph00lt0 / blocklist](https://raw.githubusercontent.com/ph00lt0/blocklists/master/blocklist.txt)
- [Scam Blocklist by DurableNapkin](https://adguardteam.github.io/HostlistsRegistry/assets/filter_10.txt)
- [ShadowWhisperer's Malware List](https://adguardteam.github.io/HostlistsRegistry/assets/filter_42.txt)
- [Stalkerware Indicators List](https://adguardteam.github.io/HostlistsRegistry/assets/filter_31.txt)
- [Steven Black's List](https://adguardteam.github.io/HostlistsRegistry/assets/filter_33.txt)
- [The Big List of Hacked Malware Web Sites](https://adguardteam.github.io/HostlistsRegistry/assets/filter_9.txt)
- [WindowsSpyBlocker - Hosts spy rules](https://adguardteam.github.io/HostlistsRegistry/assets/filter_23.txt)
- [uBlock₀ filters - Badware risks](https://adguardteam.github.io/HostlistsRegistry/assets/filter_50.txt)

## Usage (BETA)

- The python script `create_list.py` can be used to generate `aio_blocklist_final.txt` on local machine that has Python
- I have tested it on Windows 11, howevert it should work fine on other OSs too (as long as you have Python installed)

1. Download a ZIP of this repo and extract it to a suitable known folder
2. Create a new empty folder `downloaded_lists` within the `AdGuard-Home-AIO-List-main` folder
3. Edit `create_list.py` in a text editor and change line 20 to set `CURRENTWORKINGDIRECTORY` to a path where `AdGuard-Home-AIO-List-main` exists (save change)
4. Run the script `create_list.py` using Python
5. Once the script finishes add the full path of `aio_blocklist_final.txt` to AdGuard Home's `DNS blocklists` as a `custom list`
6. To regenerate the list simply run `create_list.py` when desired (as a scheduled task etc)

# Archived Old Info

The below is old info that shouldn't be needed anymore.

## ⭐ How to Add Blocklists to AdGuard Home

- If you have a PC with at least 8GB of RAM adding these lists will be very useful
- After adding and updating these lists RAM usage for AdGuard Home will go up to around 229MB

1. Log into __AdGuard Home__
2. Using the top menu click `Filters` and then `DNS blocklists`
3. Click the green `Add blocklist` button
4. Click the `Choose from the list` button
5. Checkmark the following `General` blocklists:
    - 1Hosts (List)
    - AdGuard DNS filter
    - AdAway Default Blocklist
    - Dan Pollock's List
    - OISD Blocklist Small
    - Peter Lowe's Blocklist
    - Steven Black's List
7. Checkmark the following `Other` blocklists:
    - Dandelion Sprout's Anti Push Notifications
    - WindowsSpyBlocker
9. Checkmark all of the `Security` blocklists
10. Click the green `Save` button

## ⛔ How to Block Services

1. Log into __AdGuard Home__
2. Using the top menu click `Filters` and then `Blocked services`
3. Click on the `Block all` button
4. Unblock (toggle off) services you actually use
5. Click the green `Save` button once done
