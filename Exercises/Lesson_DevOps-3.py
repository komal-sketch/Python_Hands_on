import os

print(os.system('df -h'))
print(os.system('uptime'))
print(os.system('free -h')) #RAM

#----------------------------------------------------------

command = "df -h"
command = "free -h"
command = "date"

print(command)
# it will print date because other values are variables.

def check_cpu(command):
    print(os.system(command))

    return os.system(command) #can write return in place of print

def check_ram(command):
    print(os.system(command))

    check_cpu("df -h")   #calling a function
    check_ram("free -h")

# make it shorter

def run_command(command):
    return os.system(command)

run_command("df -h")
run_command("free -h")


#----------------------------------------------------

import datetime

def show_date():
    return datetime.datetime.today()

today = show_date()
print(today)




