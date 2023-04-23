
input_time_hours = 0   # user input 
input_alarm_hours = 0 # user input
totalTime = 0  # both inputs are added
timeHour = 0 #
remainder = 0


# Print output
input_time_hours = int(input("Enter current hour: "))

input_alarm_hours = int(input("Enter alarm hours: "))

totalTime = input_time_hours + input_alarm_hours 
#Calculation
timeHour = totalTime // 24
remainder = totalTime % 24

print("The alarm will sound in", timeHour, "day(s) at", remainder,"hours") 
