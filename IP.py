# This sript prints the public IP of the device it runs into.
from urllib2 import urlopen
from time import sleep

a = 0
while True:
  my_ip = urlopen('http://ip.42.pl/raw').read()
  if my_ip != a:
    print my_ip
    a = my_ip
  # else: print("No changes")
  exit();
  sleep(3)
