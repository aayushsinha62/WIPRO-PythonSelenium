
#to execute external system commands
#interact with OS processes
#capture output, error and return codes
#control the process execution

#run the OS level commands - linux, macos windows

import subprocess

#subprocess.run() - run command and wait
#subprocess.Popen() - run process asynchronous (one by one)
#subprocess.PIPE - capture the output
#subprocess.CompletedProcess - result
# subprocess.TimeoutExpired - timeout exception
# subprocess.CalledProcessError - command failure

result=subprocess.run("dir",shell=True,capture_output=True,text=True)
print(result)

result=subprocess.run("ipconfig",shell=True,capture_output=True,text=True)
print(result)

result=subprocess.run("python --version",shell=True,capture_output=True,text=True)
print(result.stdout)
print(result.stderr)



