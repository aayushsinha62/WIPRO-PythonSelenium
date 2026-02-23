# #1.Write a Python program to sort a list of tuples using Lambda
#

data=[(1,3),(4,1),(2,3)]

sorted_data=sorted(data,key=lambda x:x[1])

print(sorted_data)

# 2.Write a Python program to extract year, month, date and time using Lambda.

from datetime import datetime

dt=datetime.now()

extract=lambda d: (d.year, d.month, d.day, d.time())

print(extract(dt))

# 3.Write a Python script to concatenate the following dictionaries to create a new one.

dict1={'a':1,'b':2}
dict2={'c':3, 'd':4}
dict3={'e':5}

new_dict={**dict1, **dict2, **dict3}
print(new_dict)

