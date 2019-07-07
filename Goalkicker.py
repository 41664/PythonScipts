import requests
from bs4 import BeautifulSoup
import wget
import os
cwd = os.getcwd() 
print("This script will download every single programming cheat sheet ever\n")
print("Expected File size- 140 MB. \n")
print("press ctrl+c to exit\n")
d=input("what directory do you want to Download books into? \n By default the script will download books in your current directory. \n Press Enter to continue \n or Enter full valid directory name\n")
if d=="":
    d='.'
try:
    os.chdir(d)
except:
    print("Not accepted. Downloading in current directory")
finally:
    os.chdir(cwd)
r=requests.get('https://books.goalkicker.com/')
soup=BeautifulSoup(r.content,'html.parser')
soup.prettify()
allbooks=soup.find_all('div',{'class':"bookContainer grow"})
for i in allbooks:
    booklink='https://books.goalkicker.com/'+i.a['href']
    print("downloading "+i.img['alt']+"\n")
    target=requests.get(booklink)
    targetsoup=BeautifulSoup(target.content,'html.parser')
    downlink=targetsoup.find('button',{'class':'download'})['onclick'][15:-1]
    wget.download(booklink+'/'+downlink)
    print("\n")
print("Thank you for using my script.")