from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections

class Mytopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        