import requests
from colorama import init,Back,Fore
init()

print(Fore.GREEN + """███████╗██████╗ ██╗██████╗ ███████╗██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗████╗ ████║██╔══██╗████╗  ██║
███████╗██████╔╝██║██║  ██║█████╗  ██████╔╝██╔████╔██║███████║██╔██╗ ██║
╚════██║██╔═══╝ ██║██║  ██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║██║╚██╗██║
███████║██║     ██║██████╔╝███████╗██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
made by 0x74ngly
####################################################################################""" + Fore.WHITE)
print("Please don't put / at the end in URL")
your_url = input("URL: ")
choose_list = int(input("""Wordlist
--------
[0] Default
[1] Custom

Option> """))

atleast_found = False
threads = 0

print("Wish granted! :)")
if choose_list == 0:
    for dir_name in open("./directory-list-2.3-big.txt","r").read().split("\n"):
        try_dir = requests.get("{}/{}".format(your_url,dir_name))
        threads += 1
        if try_dir.status_code == 200:
            print(Fore.GREEN + "Directory found: {}/{}".format(your_url,dir_name))
            atleast_found = True
    if atleast_found == False:
        print(Fore.RED + "Hmm... Try another wordlist of directories names!")
    else:
        print(Fore.GREEN + "{} directories are found in {}.".format(threads,your_url))
elif choose_list == 1:
    list_pls = input("Enter the location of wordlist: ")
    for dir_name in open(list_pls,"r").read().split("\n"):
        try_dir = requests.get("{}/{}".format(your_url,dir_name))
        threads += 1
        if try_dir.status_code == 200:
            print(Fore.GREEN + "Directory found: {}/{}".format(your_url,dir_name))
            atleast_found = True
    if atleast_found == False:
        print(Fore.RED + "Hmm... Try another wordlist of directories names!")
    else:
        print(Fore.GREEN + "{} directories are found in {}.".format(threads,your_url))