#!/usr/bin/python3
for i in range(97, 123):
    gee=chr(i)
    if gee in ['q', 'e']:
        continue
    print(gee, end='')
