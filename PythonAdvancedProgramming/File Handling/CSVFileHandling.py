
import csv

#reading csv file

with open("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#writing the csv file

with open("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//write.csv","w", newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["id","name","marks"])
    writer.writerow([1,"Rahul",85])
    writer.writerow([2,"Aayush",90])

#append the data using csv file

with open("C://Users//KIIT01//PycharmProjects//PythonAdvancedProgramming//DataFormats//data.csv","a", newline="") as file:
    writer=csv.writer(file)
    writer.writerow([3,"Kiran",85])

