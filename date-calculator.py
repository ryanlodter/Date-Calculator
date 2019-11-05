#number of days in each month
months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

#get start date
date = input("Enter start date (m-d-year): ")

dash_index = date.index('-')
month_start = int(date[:dash_index])
date = date[dash_index + 1:]

dash_index = date.index('-')
day_start = int(date[:dash_index])
date = date[dash_index + 1:]

year_start = int(date)

#get end date
date = input("Enter end date (m-d-year): ")

dash_index = date.index('-')
month_end = int(date[:dash_index])
date = date[dash_index + 1:]

dash_index = date.index('-')
day_end = int(date[:dash_index])
date = date[dash_index + 1:]

year_end = int(date)

#initialize the difference
difference = 0;

#record the number of leap years between the two dates
num_leap_years = 0;

for i in range(year_start + 1, year_end):
	if i % 4 == 0:
		num_leap_years += 1

if year_start % 4 == 0:
	if month_start < 2:
		num_leap_years += 1
		
if year_end % 4 == 0:
	if month_end >= 2:
		num_leap_years += 1

#find number of years between the two dates	
year_difference = year_end - year_start

#add the number of days between the years including the leap days
if year_difference > 0:
	difference += (365 * year_difference) + num_leap_years

#add number of days for the ending months
for i in range(month_start, month_end + 1):
	difference += months[i]
#subtract the number of days for the starting months
difference = difference - day_start
difference = difference - (months[month_end] - day_end)

#print the total difference in days
print(str(difference) + " days")
