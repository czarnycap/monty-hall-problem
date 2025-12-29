#!/usr/bin/env python3
import random
range_min = 1
range_max = 3
wybor = -1

nagroda = -1
losowan = 10000
wygrane_zmiana = 0 
wygrane_bez_zmiany = 0
przegranych = -1
debug_flag = 0
zmiana_flag = 1

for _ in range(losowan):
    wybor = random.randint(range_min,range_max)
    nagroda = random.randint(range_min,range_max) 

    if wybor == nagroda:
        wygrane_zmiana += 0
    else:
        wygrane_zmiana += 1

    if wybor == nagroda:
        wygrane_bez_zmiany += 1
    else:
        wygrane_bez_zmiany += 0

print("wygrane gdy zmiana wyboru:",wygrane_zmiana/losowan)
print("wygrane gdy brak zmiany:",wygrane_bez_zmiany/losowan)
