# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def is_leap_year(year):
	if (year%4==0) and not ((year%100==0) and not (year%400==0)):
		return True
	else:
		return False

def daysUpToDate(year,month,day):
	i=1
	while i<month:
		if i in (4,6,9,11):
			day=day+30
		if i==2:
			if is_leap_year(year):
				day=day+29
			else:
				day=day+28
		if i in (1,3,5,7,8,10,12):
			day=day+31
		i=i+1
	return day

# TEST BY LAZ
# print daysUpToDate(2011, 6, 30)
# print daysUpToDate(2012, 6, 30)

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
	days1=year1*365.25+daysUpToDate(year1,month1,day1)
	days2=year2*365.25+daysUpToDate(year2,month2,day2)
	return int(days2-days1)

# TEST BY LAZ
# daysBetweenDates(1983,5,16,2016,5,14)

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
