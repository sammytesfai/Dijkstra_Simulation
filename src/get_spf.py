'''
User interfaces with this script that will communicate with docker, python
modules, and other scipts to perform SPF on the specifed routers
'''
import os
file = open("docker-compose.yml", 'r')
ports = []
names = []
name_port_map = {}
while True:
    line = file.readline()
    if line.find('NAME') != -1:
        names.append(line.split('=')[1].split('\r')[0].split('\n')[0])
    if line.find('ports') != -1:
        line = file.readline()
        ports.append(line.split(':')[0].split('"')[1])
    if not line:
        break

for (port, name) in zip(ports, names):
    name_port_map[name] = port

print("Welcome to Sammy Tesfai's CSE 151 Project!\n\n")
while True:
    print("Which router would you like to run Dijkstra's SPF on:\n")
    for i in range(1, len(names)+1):
        print("{}. {}".format(i, names[i-1]))

    print('')
    val = input("(Enter router name): ")
    
    print("Results: \n")
    port = name_port_map.get(val)
    if port:
        os.system('curl http://127.0.0.1:{}/dijkstra'.format(port))
        print('')
        cont = input("Would you like to run this again? (yes/y or no/n) ")
        if cont == 'no' or cont == 'n':
            break
        print('')
    else:
        print('You have entered an incorrect router name.')
