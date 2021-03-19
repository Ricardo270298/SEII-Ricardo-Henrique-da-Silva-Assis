import datetime
import pytz

# Naive
 d = datetime.date(2014, 6, 12)
	print(d )
tday = datetime.date.today()
	print(tday.weekday()) # Monday = 0; Sunday = 6
	print(tday.isoweekday())  # Monday = 1; Sunday = 7

tdelta = datetime.timedelta(days=7)
	print(tday - tdelta)

 datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

tdelta = datetime.timedelta(hours=12)

 print(tday + tdelta)

 date2 = date1 + timedelta
 timedelta = date1 + date2

bday = datetime.date(2016, 9, 24)

till_bday = bday - tday

 print(till_bday.days)

t = datetime.time(9, 30, 45, 100000)

 dt_today = datetime.datetime.today()
 dt_now = datetime.datetime.now()
 dt_utcnow = datetime.datetime.utcnow()
 print(dir(datetime.datetime))
 print(dt_today)
 print(dt_now)
 print(dt_utcnow)

dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
 print(dir(dt))

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
 print(dt_utcnow)

dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
 print(dt_utcnow2)

 dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
 print(dt_mtn)

for tz in pytz.all_timezones:
	print(tz)

dt_mtn = datetime.datetime.now()

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)

 print(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
 print(dt_east)

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

 strftime - Datetime to String
 strptime - String to Datetime
