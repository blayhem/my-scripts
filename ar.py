# This script prints every IP connected to the router (every 2s)
# TODO: print only changes.
from os import system
from time import sleep
while True:
  system('arp -a')
  print ("")
  sleep(2)

