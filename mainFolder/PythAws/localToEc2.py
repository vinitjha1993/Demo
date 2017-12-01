
import subprocess
import os
p = subprocess.Popen(["scp", '/home/bridgeit/Downloads/vinitkeypair.pem /home/bridgeit/Desktop/ht/b.txt', 'ubuntu@35.154.233.181:/home/ubuntu/pycharm'])
sts = os.waitpid(p.pid, 0)
print("uploaded")
scp.c
'''import shutil
try:
    shutil.copy('/home/bridgeit/Downloads/vinitkeypair.pem /home/bridgeit/Desktop/ht/b.txt', 'ubuntu@35.154.233.181:/home/ubuntu/pycharm')
except BaseException as e:
    print(e)

print("uploaded")'''