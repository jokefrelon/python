from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController, CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections


class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        Pcs = []
        Switchs = []

        for Sw in range(1, 5):
            re = self.addSwitch('Switch{}'.format(Sw))
            Switchs.append(re)
        for pc in range(1, 6):
            re = self.addHost('Pc{}'.format(pc))
            Pcs.append(re)
        IPhoneSE = 0
        for isu in range(0, 2):
            self.addLink(Switchs[IPhoneSE], Pcs[isu])
        IPhoneSE += 1

        for tuplew in range(2, 4):
            self.addLink(Switchs[IPhoneSE], Pcs[tuplew])
        IPhoneSE += 1
        for qwe in range(0, 2):
            self.addLink(Switchs[IPhoneSE], Switchs[qwe])

        self.addLink(Switchs[IPhoneSE], Switchs[-1])
        self.addLink(Switchs[-1], Pcs[-1])


topos = {'mytopo': (lambda: MyTopo())}

#注意：‘mytopo’这个参数必须和命令行--topo的参数一致，如果不一致，运行时报“Exception: Invalid topo name xxx