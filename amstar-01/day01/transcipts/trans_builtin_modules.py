Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> t = datetime.datetime.now()
>>> t
datetime.datetime(2020, 2, 4, 5, 14, 51, 687724)
>>> t.year
2020
>>> t.month
2
>>> t.day
4
>>> t.hour
5
>>> t.minute
14
>>> t.second
51
>>> temp = "%A, %d. %B %Y %I:%M%p"
>>> temp1 = "%A, %B %d, %Y %H:%M:%S"
>>> t
datetime.datetime(2020, 2, 4, 5, 14, 51, 687724)
>>> t.strftime(temp)
'Tuesday, 04. February 2020 05:14AM'
>>> t.strftime(temp1)
'Tuesday, February 04, 2020 05:14:51'
>>> 
 RESTART: C:/Users/Purushotham/Desktop/Clients/Amstar/Oracle Py 01/profiler.py 
........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................It took  0:00:14.330343
>>> 
