userName="Hello <<UserName>>, How are you"
name=input("enter username")
if len(name)>3:
    print(userName.replace("<<UserName>>",name))
else:
    raise Exception('enter name of more than 3 character')


