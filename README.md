# Dijkstra Simulation


## Modules
- get_spf.py
    - Parses the compose file to identify the current nodes and ports being used and creates a mapping from name to port. Also interfaces with user to perform SPF on a specific router. Formulates curl request using the name provided by user and outputs calculated SPF for all other routers in domain.  
- router.py
    - REST API (Flask) that responds to client requests in order to calculate and perform Dijkstras SPF algorithm and responds to the client with the cost to all other nodes in routing domain with the cheapest cost to the destination.
- node.py
    - Class module to hold specific router information for all routers in the the domain. Holds SPF information, local link cost, and local ip information. 
- misc.py
    Miscellaneous module that performs broadcast communication with all other nodes in domain and helper function to print spf output in a more readable manner.

## Example
- Start the docker daemon
- Once docker daemon is running in background enter [`docker compose up`] in a terminal that is currently in the top directory of this pproject. This will create images and containers for all the routers.
- Once all routers are active and waiting for incoming request on a seperate terminal we will call our client module with [`python3 get_spf.py`] (**This module requires python3 to operate**)
- Once executed the program will prompt the user to enter the name of the router to perform SPF on. Refer to the compose file for current router names and enter the name exactly as it is this file. The program will then output the cheapest cost to all other nodes relative to the node mentioned.
The program will then prompt the user to either continue the program and get SPf output for another node or terminate the program.
- A bash script is also provided to clean up currently running docker containers and images. Simply call [`./bin/run_docker.sh`] at the top level directory.

## Topology

![Current topology implemented in compose file.](doc/Topo.jpg)
