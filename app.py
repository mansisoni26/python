ulist=[]
print('''User Authentication Application
1. Sign up
2. Log in
3. Delete user
4. Exit...''')
while(True):
	choice=int(input("choice"))
	if choice==1:
		user={}
		user['name']=input("enter name:")
		user['pass']=input("enter password:")
		user['email']=input("enter email:")
		ulist.append(user)
	if choice==2:
   		uname=input("name=")
   		upass=input("pswd")
   		for u in ulist:
       		if(u['name']==uname):
       			if(u['pass']==upass):	
       				print("Login successfull")
       		else:
       			print("Login failed")
    	else:
      		 print("Wrong username")  
	if choice==3:
    	username=input("Enter user whom you want to delete:")
    for u in ulist:
        if u['user']==username:
           	ulist.remove(u)
           	print("user deleted")
	if choice==4:
  		 print("exit")           




