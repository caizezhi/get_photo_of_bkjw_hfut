import os
while 1:
    year = 2013
    NO = 210000
    numbers = year * 1000000 + NO
    for year in range(2013, 2015):
        for NO in range(210000, 2200000):
            com = 'wget http://bkjw.hfut.edu.cn/student/photo/' + str(year) + '/' + str(numbers) + '.jpg'
            os.popen(com)
            numbers = numbers + 1
            NO = NO + 1
        year = year + 1
