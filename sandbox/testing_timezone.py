"""Module testing getting the current datetime for sydney, australia."""

# import time
from datetime import datetime
from pytz import timezone
# import pytz

#DATETIME = datetime.now()
#TIMEZONE = "UTC"
#DATETIME = DATETIME.now(timezone(TIMEZONE))
#DATETIME.strftime('%X')
#print(DATETIME.now(timezone(TIMEZONE)).today())

# Shows all timezones
#print('Timezones')
#for timeZone in pytz.all_timezones:
#    print(timeZone)

au_tz = timezone('Australia/Sydney')

loc_dt = au_tz.localize(datetime.now())

# Convert localized date into Australia/Sydney timezone
au_tz = timezone('Australia/Sydney')
print(loc_dt.astimezone(au_tz))
