import os, requests
DOMAIN = os.getenv('DOMAIN').split(',')
IP = os.getenv('IP')
LINKS = os.getenv('LINKS').split(',')
NAME = os.getenv('NAME')

def Query_Link_Costs():
    resp = {}
    for addr in DOMAIN:
        if addr != IP:
            try:
                msg = requests.get(url='http://' + addr + '/router', timeout=5)
                resp[addr] = msg.json()['costs']
            except requests.exceptions.Timeout:
                resp[addr] = "error"
            except requests.exceptions.TooManyRedirects:
                resp[addr] = "error"
            except requests.exceptions.RequestException:
                resp[addr] = "error"
    return resp

def print_pretty(dist):
    output = 'Router: {}\n\n'.format(NAME)
    for ip in dist:
        output += 'Destination: {}, \t SPF Cost: {}\n'.format(ip.split(':')[0], dist[ip])

    return output
