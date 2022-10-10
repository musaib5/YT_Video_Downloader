from pytube import YouTube
from sys import argv
import os     # provides OS interaction utility 
import pathlib    #Pathlib module in Python provides various classes representing file system paths with semantics appropriate for different operating systems.
from datetime import date

    #link= argv[1] #argv used to run this program from command line

link= input("Enter the link of the video : ")
print("\n")
yt= YouTube(link) #created  YouTube object named yt to be used further down the line.


print("Title:", yt.title)


print("Views: ", yt.views)
print("\n")

yd= yt.streams.get_highest_resolution() #Get the highest res version   

    # dt_path= str(os.environ['USERPROFILE'] + '\Desktop')
    # # print(dt_path) #prints your desktop path.

    # down_path = dt_path.replace("\\", "/")
    # print(down_path)   

    # yd.download("down_path")

today= str(date.today())

down_dir= str(input(r"Enter the location path where download folder is to be created: "))
print("\n")

name_folder= input("Name your download folder where video is to be saved: ")
print("\n")
os.chdir(down_dir)  #specifying(change directory)  path where folder is to be created (we have taken user input above)

os.mkdir(today+ "-"+ name_folder) #create folder with name in the argument.


yd.download(today+ "-"+ name_folder)






