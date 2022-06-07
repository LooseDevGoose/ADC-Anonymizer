import re
import os
import random

# Get current working directory
current_path = os.getcwd()

# Generate random number and rewrite matches
def rewrite_ip(text):

    ip_removal = re.sub(
        "[1-9][0-9]{1,3}", f"{str(random.randrange(1, 255))}", text)

    hash_removal = re.sub(
        "[0-9a-fA-F]{80,160}", f"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", ip_removal)
    print(hash_removal)

    return (str(hash_removal))


# Get all .conf files from current directory
for root, dirs, files in os.walk(f"{current_path}"):
    for file in files:
        if file.endswith(".conf"):

            #Rename file to .txt for editing
            os.rename(file, "ns.txt")

            #Open file and save text to variable
            f = open("ns.txt", "r")
            text = (f.read())
            #Replace IP's with fake data
            anonymous_text = rewrite_ip(text)
            f.close()

            #Write back to file
            f = open("ns.txt", "w")
            f.write(anonymous_text)
            f.close()
            #Rename file back to .conf
            os.rename("ns.txt", "ns.conf")
