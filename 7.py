#!/usr/bin/env python3

distance = 10
distance_sum_seven_day = 10
distance_sum_n_day = 10
n = int(input('Enter count days:'))
print('a)')

for day in range(9):
	distance = distance + (distance/10)
	if(day < 6):
		distance_sum_seven_day += distance
	if(day < n - 1):	# потому что итерации идут с нуля
		distance_sum_n_day += distance
	print('   Day', day+2, ' - ', int(distance) )
	
print('b)', distance_sum_seven_day)
print('c)', distance_sum_n_day)

distance = 10
for day in range(21):
	distance = distance + (distance/10)

print('d) day', day, '|','distance =', int(distance),'|', 'You will must stop run!')
