
#used to loop over an iterable
#gets both index and value at same time

#enumerate with list/strings/tuples

#for list
#
# enumerate(list,start=0)

fruits=["orange", "cherry", "kiwi"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# enumerate with start value changed

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

word="python"
for index, ch in enumerate(word):
    print(index,ch)

#enumerate with tuple

fruits=("orange", "cherry", "kiwi")

for index, fruit in enumerate(fruits):
    print(index, fruit)

#real time scenarios

test_cases=["login", "signup", "checkout"]
for case_no, test in enumerate(test_cases, start=1):
    print(f"executing testcase {case_no}: {test}")

a=['God','is','Great']
b=enumerate()
nxt_val=next(b)
print(nxt_val)

#duplicate detection using enumeration

characters=["Krillin", "Goku", "Goku", "Gohan", "Piccolo", "Krillin", "Goku", "vegeta", "Goku" ,"Goku"]

character_map={character: [] for character in set (characters)}
for index, character in enumerate(characters):
    character_map[character].append(index)

print(character_map)


