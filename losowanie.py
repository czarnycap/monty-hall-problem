#!/usr/bin/env python3
import random
a = 1
b = 0
c = 0

wybor = -1
losowan = 1000
wygranych = 0
wygranych_procent = 0
bramki = [a, b, c]


for i in range(losowan):
#    print(i)
    wybor = random.randint(0,2)
    a = random.randint(0,1)
    b = random.randint(0,1)
    c = random.randint(0,1)
    bramki = [a,b,c]
    print(bramki)
    if wybor == bramki[wybor]:
        wygranych += 1

wygranych_procent = wygranych / losowan
print("ile bylo wygranych",wygranych)
print("ile procent wygranych",wygranych_procent)


        

