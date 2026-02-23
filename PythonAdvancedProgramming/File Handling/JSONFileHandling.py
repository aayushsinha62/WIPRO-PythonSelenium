import json

try:
    with open("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//emplyee.json",'r') as file:
        data=json.load(file)

except FileNotFoundError:
    print("file doesnt exists")

print(data)

with open("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//nested.json",'r') as file:
    data=json.load(file)


email=data["user"]["profile"]["email"]
print(email)

#writing to json file : dump method
#in reading load was used


data= {
  "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}

with open("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//write.json",'w') as file:
    json.dump(data,file)

#update or modify

with open("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//update.json",'r') as file:
    data=json.load(file)

data["experience"]=6

with open("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//update.json",'w') as file:
    json.dump(data, file, indent=4)

