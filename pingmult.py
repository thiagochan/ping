import os

hosts = ["google.com", "8.8.8.8", "4.4.4.4", "brasil.com"]

txt = open('hosts.txt', 'w')
for h in range(len(hosts)):
    txt.write(f'{hosts[h]}\n')
txt.close()

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        os.system('ping '+ ip)