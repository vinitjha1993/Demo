
import paramiko

key = paramiko.RSAKey.from_private_key_file('/home/bridgeit/Downloads/vinitkeypair.pem')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance
try:
    # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
    client.connect(hostname='13.127.37.241', username="ubuntu", pkey=key)

    # Execute a command(cmd) after connecting/ssh to an instance
    #stdin, stdout, stderr = client.exec_command('ls ./folder1')
    stdin, stdout, stderr = client.exec_command('aws s3 cp s3://vinn/h.html /home/ubuntu/folder1/h1.html')
    print(stdout.read())

    # close the client connection once the job is done
    client.close()


except BaseException as e:
    print(e)