import datetime
import calendar

#a)
def last_day_of_month(month):
	c = calendar.Calendar(firstweekday=0)
	days = list(c.itermonthdays(month.year, month.month))
	negative_days = 1
	while not days[-negative_days]>0:
		negative_days += 1
	print(days[-negative_days])
	return datetime.datetime(month.year, month.month, days[-negative_days])
#a (zweite Lösung)
def last_day_of_month2(month):
	return datetime.datetime(month.year, month.month, calendar.monthrange(month.year, month.month)[1])

#b)
def number_of_workdays(day1, day2):
	workdays = 0
	day = datetime.timedelta(days=1)

	while day1 <= day2:
		for i in range(0,5):
			if day1.weekday() == i:
				workdays += 1
		day1 += day
	print(workdays)