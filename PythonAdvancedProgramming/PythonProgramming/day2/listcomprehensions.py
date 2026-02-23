#comprehension-create list using single line of code instead of loops

#syntax we write in one line

#square of a number

sqs=[x**2 for x in range(1,6)]
print(sqs)

#with the condition

evennumbers=[x for x in range(10) if x%2==0]
print(evennumbers)

#dictionary comprehension - increase by 10%

salary = {"A":50000, "B":60000, "C":76000}
updated_sal={key:value+0.1*value for key,value in salary.items()}
print(updated_sal)

#filtering of dictionary

employees={
    "Harsha":"ACTIVE",
    "Amit":"INACTIVE",
    "Ravi":"ACTIVE"
}

active_employees={k:v for k,v in employees.items() if v=="ACTIVE"}
print(active_employees)


#set comprehension

#same just curly braces

sqs={x**2 for x in range(1,6)}
print(sqs)

#can be done using tuples, strings

