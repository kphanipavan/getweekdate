# Get Week Date
This program will print the date as per user's requirement like 'next friday', 'previous monday', 'next week's sunday', etc...

# Usage
The file 'day.py' is copied into your project's directry.

The file is then imported using the following statement:

>from day import *

You can call the function 'get_weekdate' as following:

>get_weekdate(day, day_type, referrence_date)

day - which day you want to get, sunday, monday, tuesday....

day_type - you need next week day, next week's week day, previous week day, previous week's week day

referrence_day - enter the referrence day in a fixed format as a string: 'yyyy-mm-dd', leave it empty to take today's date as referrence

# Examples

get_weekdate('tuesday', 'next')

get_weekdate('SuNdAy', 'next_week', '2020-3-20')

get_weekdate('Saturday', 'pReviouS', '2001-5-1')

get_weekdate('Monday', 'pReviouS_weeK')


P.S: The text is not case sensitive. The date must be in proper format.
