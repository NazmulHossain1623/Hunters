#!/usr/bin/python2
#coding=utf-8
#The THIS TOOLS MADE BY NAZMUL HOSSAIN 
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

#Dev: NAZMUL_HOSSAIN
##### LOGO #####
logo = """

███╗   ██╗ █████╗ ███████╗███╗   ███╗██╗   ██╗██╗     
████╗  ██║██╔══██╗╚══███╔╝████╗ ████║██║   ██║██║     
██╔██╗ ██║███████║  ███╔╝ ██╔████╔██║██║   ██║██║     
██║╚██╗██║██╔══██║ ███╔╝  ██║╚██╔╝██║██║   ██║██║     
██║ ╚████║██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝███████╗
╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝
\033[1;96m|-------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-----|
\033[1;96m|               WELCOME BUDY               |
\033[1;96m| THIS TOOLS MADE FOR BD TASLA TEAM OWNERS|
\033[1;96m|------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+------|
\033[1;91m [⚡\033[1;97mAUTHOR NAME: NAZMUL        ⚡\033[1;91m]
\033[1;91m [⚡\033[1;97mFACEBOOK   : NAZMUL HOSSAIN ⚡\033[1;91m]
\033[1;91m [⚡       \033[1;97mFROM: BD            ⚡\033[1;91m]
\033[1;95m«-_-_-_-_-_-_-_-_-\033[1;91mNAZMUL \033[1;95m-_-_-_-_-_-_-_-_-»
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;91m░██╗░░░░░░░██╗███████╗██╗░░░░░
\033[1;91m░██║░░██╗░░██║██╔════╝██║░░░░░
\033[1;91m░╚██╗████╗██╔╝█████╗░░██║░░░░░
\033[1;91m░░████╔═████║░██╔══╝░░██║░░░░░
\033[1;91m░░╚██╔╝░╚██╔╝░███████╗███████╗
\033[1;91m░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝
\033[1;91m░█████╗░░█████╗░███╗░░░███╗███████╗
\033[1;91m██╔══██╗██╔══██╗████╗░████║██╔════╝
\033[1;91m██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
\033[1;91m██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
\033[1;91m╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
\033[1;91m░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
\033[1;95m«-_-_-_-_-_-_-_-_-\033[1;91mNAZMUL \033[1;95m-_-_-_-_-_-_-_-_-»
\033[1;92mNote1: ENTER TOOL USERNAME AND PASSWORD 
\033[1;92mNote2: THIS TOOLS MADE BY NAZMUL HOSSAIN
\033[1;95m«--_-_-_-_-_-_-_-\033[1;91m  TASLA  \033[1;95m-_-_-_-_-_-_-_-_-»
 """
CorrectUsername = "BD"
CorrectPassword = "TASLA TEAM"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m \x1b[1;91mTool Username \x1b[1;91m: \x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m \x1b[1;91mTool Password \x1b[1;91m: \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev: Nazmul_Hossain
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;93mWrong Password"
            os.system('xdg-open https://www.facebook.com/NazmulHossain16239')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/NazmulHossain16239')
        

print "\033[1;93m █▓▒­░⡷ 𝗚𝗥𝗘𝗔𝗧 ⢾░▒▓█"
print "\033[1;93m █▓▒­░⡷ 𝐂𝐎𝐌𝐌𝐀𝐍𝐃 𝐈𝐍𝐒𝐓𝐀𝐋𝐋 𝐃𝐎𝐍𝐄 ⢾░▒▓█"
print "\033[1;93m █▓▒­░⡷ 𝗡𝗢𝗪 𝗧𝗬𝗣𝗘 [   sh install.sh   ] ⢾░▒▓█"
print "\033[1;93m █▓▒­░⡷ 𝙰𝙽𝙳 𝙿𝚁𝙴𝚂𝚂 𝙴𝙽𝚃𝙴𝚁 ⢾░▒▓█"

