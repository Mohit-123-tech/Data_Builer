from os import system

n = 0
i = 1
system("tar -czf data_0.tar.gz data_")
while(i<=1000):
    system(f"tar -czf data_{i}.tar.gz data_{n}.tar.gz")
    n = n+1
    i = i+1
    if i == 1001:
        break

m = 999
while(m>=0):
    system(f"rm -d -r data_{m}.tar.gz")
    m = m-1
