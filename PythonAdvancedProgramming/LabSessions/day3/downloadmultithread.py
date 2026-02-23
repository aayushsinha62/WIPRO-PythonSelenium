import threading
import time

def download_file(file_name):
    print(("downloading the file"))
    time.sleep(2)
    print(f"{file_name} downloaded")

file=["file1.txt", "file2.txt", "file3.txt"]

threads=[threading.Thread(target=download_file,args=(file,)) for file in file]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()