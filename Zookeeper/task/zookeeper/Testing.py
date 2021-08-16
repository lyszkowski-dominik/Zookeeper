# put your python code here
hour1 = input()
hour1 = int(hour1)
minutes1 = input()
minutes1 = int(minutes1)
seconds1 = input()
seconds1 = int(seconds1)
hour2 = input()
hour2 = int(hour2)
minutes2 = input()
minutes2 = int(minutes2)
seconds2 = input()
seconds2 = int(seconds2)

hourdiff = (hour2 - hour1) * 60
minutediff = (minutes2 - minutes1 + hourdiff) * 60
secondsdiff = seconds2 - seconds1 + minutediff
print(secondsdiff)