#To shudown pc
import os
lists=['Shutdown','Switch user(log out)']
for i in range(len(lists)):
    print(str(i+1)+". "+lists[i])
user_option=int(input("Your Choice(1/2):- "))
if(user_option==1):
    os.system("shutdown /s /t 1")
elif(user_option==2):
    os.system("shutdown /l")
else:
    print("Invalid option choosen")

"""
Explanation:-
This code is defined to automate the task of switching off or changing user(loging out of microsoft account)
1.We will be using OS library 
2.We created a list(Name:-lists) to store the menu content
3.system is a function in os library in which as a parameter we use "shutdown" along it we need to  use "/s" "/t" 1 to tell system to shutdown the system
4.Same like that "\l" denotes re starting
"""
#Thanks a lot for viewing contribute by:- Hemang Jiwnani

