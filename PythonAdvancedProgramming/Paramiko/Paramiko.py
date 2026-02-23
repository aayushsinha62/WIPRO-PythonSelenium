import paramiko

host="localhost"
port=22
username="kiit01"
password="admin"

#create object and connect to remote machines
client=paramiko.SSHClient()

#set the rule to handle the unknown host keys
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname=host,
    port=port,
    username=username,
    password=password
)

stdin,stdout,stderr=client.exec_command("whoami")
print(stdout.read().decode())
client.close()