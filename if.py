#!/usr/bin/python3

from requests import get
import subprocess,time,pyspeedtest
import webbrowser #It will open default browser
options="""
    Press 1 to start your default browser:
    Press 2 to check your internet connection speed:
    Press 3 to check your internet status:
    Press 4 to check current date and time:
    Press 5 to check current temperature in your city:
    Press 6 to check current public IP:
    Press 7 to create a directory in your OS:
    Press 8 to reboot your system:
    Press 9 to play song in youtube:
    Press 10 to search something in google search engine:"""

print (options)
#accept input from the user
choice=input() #input function accept input in string form only

print("YOu have entered ",choice)
#conditional statements
if choice == '1' :
    print("Plzz wait...Browser is opening")
    time.sleep(2)
    #opening the default browser
    webbrowser.open_new_tab('https://www.google.com')

elif choice == '2' :
    st = pyspeedtest.SpeedTest()
    st.ping()
    st.download()
    st.upload()

elif choice == '3' :
     output = subprocess.getstatusoutput('ping -c 2 8.8.8.8')
     if output[0] == 0 :
            print("Internet is working fine...")
     else : 
            print("Internet is not working...")

elif choice == '4' :
    print("Current date and time: ",subprocess.getoutput("date"))

elif choice == '5' :
    city = input("Enter your city to find its current temperature: ")
    #opening default browser
    webbrowser.open_new_tab('https://www.google.com/search?q=city')

elif choice == '6' :
    myip = get('https://api.ipify.org').text
    print('My Public IP: {}' .format(ip))

elif choice == '7':
    #Asking for directory name
    dir_name = input("Plzz enter directory name: ")
    dir_output = subprocess.getstatusoutput("mkdir ",dir_name)
    if dir_output[0] == 0:
        print("Your directory "+dir_name+" is successfully created")
    else:
        print("Plzzz choose another name for directory")

elif choice == '8':
    subprocess.getoutput('reboot')

elif choice == '9':
    song = input("Enter song to play: ")
    subprocess.getoutput(('https://www.youtube.com/results?search_query='+song))

elif choice == '10':
    msg = input("Plzz enter msg to search on Google: ")
    time.sleep(2)
    #Opening default browser
    webbrowser.open_new_tab('https://www.google.com/search?q='+msg)

else :
    print("Wrong choice!!")
