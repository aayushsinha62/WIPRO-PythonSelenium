#destructors - when we want to destroy the object
#post conditions like closing of the browser, db connection closing
   #releasing of certain resources, cleanup operations
#for efficient memory usage, destructors should be used
#when DB connection has to be closed

#free the memory (garbage collection) which is automatically called

class Desct:

    def __init__(self):
        print("object created")

    def __del__(self):
        print("Closing the DB connection")


a=Desct()
print("End of program")
del a

#desctructor in file handling

class FileHandler:
    def __init__(self,filename):
        self.file=open(filename,'w')
        print("file is opened")


    def readfile(self,filename):

        print("file is being read")

    def __del__(self):
        self.file.close()
        print("file closed")

f=FileHandler("test.txt")
del f