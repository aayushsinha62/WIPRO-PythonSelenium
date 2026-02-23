#sets dont allow duplicate elements i.e contains only unique data
#unordered collection
from PythonProgramming.day1.lists import mixeddata

#create student_id set integer type
stu_id={112,112,114,115}
print(stu_id)

#string type set
letters={'a','b','c','d','e'}
print(letters)

#create a mixed set
mixed_set={"Hello",1,2,3}
print(mixed_set)

empty_set=set()
print(empty_set)

stu_id.add(116)
print(stu_id)

stu_id.update([3,4,5])
print(stu_id)

stu_id.remove(112)
print(stu_id)

stu_id.discard(112)
print(stu_id)

stu_id.pop()
print(stu_id)

stu_id.clear()
print(stu_id)

anotherid={119,110, 112}
print(stu_id.union(anotherid))

print(stu_id.intersection(anotherid))

print(stu_id.difference(anotherid))

print(stu_id.symmetric_difference(anotherid)) ##returns non common elements

print(stu_id.issubset(anotherid))

print(stu_id.issuperset(anotherid))

print(stu_id.isdisjoint(anotherid))



