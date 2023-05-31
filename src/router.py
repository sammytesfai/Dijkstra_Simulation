'''
Routers perform dijkstra alogorithm and respond to client requests as well as 
peer requests for local SPF information
'''

from flask import Flask, request
import os, node, misc


DOMAIN = os.getenv('DOMAIN').split(',')
IP = os.getenv('IP')
LINKS = os.getenv('LINKS').split(',')
MAX = 99999

router_store = node.node(IP, DOMAIN, LINKS)
app = Flask(__name__)

def minDistance(dist, sptSet):
    min = MAX
    min_index = None

    for ip in DOMAIN:
        if sptSet[ip] == False and dist[ip] <= min:
            min = dist[ip]
            min_index = ip

    return min_index

@app.route("/router", methods = ['GET'])
def get_peer_costs():
    return {'costs': router_store.get_spf()[router_store.get_ip()]}, 200
        
# Used the below website for reference:
# https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
@app.route("/dijkstra", methods = ['GET'])
def dijkstra():
    peer_links = misc.Query_Link_Costs()
    spf = router_store.get_spf()
    for peer in peer_links:
        spf[peer] = peer_links[peer]
    
    dist = {}
    sptSet = {}
    for ip in DOMAIN:
        dist[ip] = MAX
        sptSet[ip] = False
    dist[IP] = 0

    for i in range(0, len(DOMAIN) - 1):
        min = minDistance(dist, sptSet)
        sptSet[min] = True
        
        for ip in DOMAIN:
            weight = 0
            if spf[min].get(ip):
                weight = spf[min].get(ip)
            if not sptSet[ip] and spf[min].get(ip) and dist[min] != MAX and (dist[min] + weight) < dist[ip]:
                dist[ip] = dist[min] + weight

    return misc.print_pretty(dist), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 13800)