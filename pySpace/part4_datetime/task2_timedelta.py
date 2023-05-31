import pytz
from datetime import datetime

def time_diff(timestamp1, timestamp2):
    return int(-(-(timestamp1 - timestamp2).total_seconds() //1))

timezone_newyork= pytz.timezone('America/New_York')
timezone_london = pytz.timezone("Europe/London")
newyorkDateTime = datetime(2013, 3, 15, 10, 6, 10,2300)
londonDateTime = datetime(2013, 3, 15, 10, 5, 10,623)
datewith_tz_newyork = timezone_newyork.localize(newyorkDateTime)
datewith_tz_london = timezone_london.localize(londonDateTime)

print(time_diff(datewith_tz_newyork,datewith_tz_london))


# print(datewith_tz_newyork.timestamp())
# print(int(datewith_tz_london.timestamp()))


# delta = datewith_tz_newyork - datewith_tz_london
# print(delta.total_seconds())
# ee_zone = pytz.timezone(pytz.country_timezones['ee'][0])
# now = ee_zone.localize(datetime.now())
# current_date = datetime.now().time()
# current_date = current_date.replace(tzinfo=datetime.timezone.utc)

# for timezone in pytz.all_timezones:
#     print(timezone)
# date1 = datetime.now(pytz.timezone('Africa/Abidjan'))
# date2 = datetime.now(pytz.timezone('America/Aruba'))
# date3 = datetime(2023,5,20,10,0,0,tzinfo= pytz.timezone('Europe/Riga'))
# date4 = datetime(2023,5,20,10,0,0,tzinfo= pytz.timezone('Europe/Tallinn'))
# date5 = datetime(2015,10,20,20,00,tzinfo= pytz.timezone('Turkey'))
# date6 = datetime(2015,10,20,19,00,tzinfo= pytz.timezone('Pacific/Pitcairn'))
# date7 = datetime(2013,2,15,14,15,0)
# date8 = datetime(2013,2,15,10,15,0)

# print(date3.timestamp())
# print(date4.timestamp())

# delta2 = date3 - date4
# print(delta2.total_seconds()) # 900?
# delta1 = date1 - date2
# delta3 = date5.timestamp()- date6.timestamp()
# delta4 = date7 - date8
# print(delta1.total_seconds()) #0
# print(delta3.total_seconds()) #3600
# print(delta4.total_seconds()) #14400
# print(date1)
# print(date2)
# if current_date.tzinfo == None or current_date.tzinfo.utcoffset(current_date) == None:
#     print("Unaware")
# else:
#     print("Aware")
# print(ee_zone)
# print(now)
# now
# datetime.datetime(2018, 10, 9, 12, 59, 49, 109639)
