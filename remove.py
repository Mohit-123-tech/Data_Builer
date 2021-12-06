from os import system

m = 1000
while(m>=0):
    system(f"rm -d -r data_{m}.tar.gz")
    m = m-1
