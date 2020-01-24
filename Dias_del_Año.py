def isYearLeap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            return False
        return True
    else:
        return False  

def daysInMonth(year, month):
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    if isYearLeap(year)==True:
        dias[1]=dias[1]+1
    return dias[month-1]

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")