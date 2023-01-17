import calendar

n=input().split()
MM=int(n[0])
DD=int(n[1])
YYYY=int(n[2])

A=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(A[calendar.weekday(YYYY, MM, DD)])
