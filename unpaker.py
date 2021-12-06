from os import system

i = 1000
while(i>=0):
    system(f'tar -xvzf data_{i}.tar.gz')
    i = i-1
    if (i == 0):
        break

