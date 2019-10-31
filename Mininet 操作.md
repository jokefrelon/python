# Mininet 操作

### mininet建立拓扑



##### 最简单的方式,两个switch 两个pc

~~~shell
sudo mn
~~~



##### 最小的网络拓扑，一个交换机下挂两个主机

~~~shell
sudo mn --topo minimal
~~~



##### 每个交换机连接一个主机，交换机间相连接

~~~shell
sudo mn --topo linear,4
~~~



##### 每个主机都连接到同一个交换机上

~~~shell
sudo mn --topo single,3
~~~



##### 定义深度和扇出形成基于树的拓扑

~~~shell
sudo mn --topo tree, fanout=2,depth=2 --controller remote --switch ovsk,protocols=OpenFlow13
~~~

### 互交界面操作

##### 添加主机

~~~shell
py net.addHost('h3')
~~~



##### 添加Switch

~~~shell
py net.addSwitch("s2")
~~~



##### 把主机添加到Switch

~~~shell
py net.addLink(s1,net.get('h3'))
~~~



##### 给Switch S1 添加端口eth3 用于连接h3

~~~shell
py s1.attach('s1-eth3')
~~~



##### 给pc添加IP地址

~~~shell
py net.get('h3').cmd('ifconfig h3-eth0 10.0.0.3')
~~~



##### pc 互 ping

~~~shell
h1 ping h3
~~~





### mininet常用命令
|           nodes           |               显示节点列表                |
| :-----------------------: | :---------------------------------------: |
|            net            |               显示网络拓扑                |
|           dump            | 显示每个节点的接口设置和表示每个节点的PID |
|    [node id] ifconfig     |          查看node节点的网络配置           |
|      [node id] route      |            查看该节点的路由表             |
| iperf [node id] [node id] |         查看两个节点间的网络性能          |
| [node id] ping [node id]  |         测试两个节点间的网络连通          |
|          pingall          |              ping所有的节点               |
|      xterm [node id]      |        启动登陆到该节点的远程xterm        |

### 使用python脚本自定义拓扑

1.  --topo linear,4

~~~python
from mininet.net import Mininet
from mininet.topo import LinearTopo
Linear4 = LinearTopo(k=4)    #四个交换机，分别下挂一个主机
net = Mininet(topo=Linear4)
net.start()
net.pingAll()
net.stop()
~~~



2.  --topo single, 3

    ~~~python
    from mininet.net import Mininet
    from mininet.topo import SingleSwitchTopo
    Single3 = SingleSwitchTopo(k=3)   #一个交换机下挂3个主机
    net = Mininet(topo=Single3)
    net.start()
    net.pingAll()
    net.stop()
    ~~~



3.  --topo tree,depth=2,fanout=2

    ~~~python
    from mininet.net import Mininet
    from mininet.topolib import TreeTopo
    Tree22 = TreeTopo(depth=2,fanout=2)
    net = Mininet(topo=Tree22)
    net.start()
    net.pingAll()
    net.stop()
    ~~~

    

4.  如果是非上述三种类型的拓扑，那么下面介绍一种适合各种拓扑形式的脚本创建模式。本例：1个交换机，2个主机，并且赋予主机IP地址。

~~~python
from mininet.net import Mininet
net = Mininet()
# Creating nodes in the network.
c0 = net.addController()
h0 = net.addHost('h0')
s0 = net.addSwitch('s0')
h1 = net.addHost('h1')
# Creating links between nodes in network
net.addLink(h0, s0)
net.addLink(h1, s0)
# Configuration of IP addresses in interfaces
h0.setIP('192.168.1.1', 24)
h1.setIP('192.168.1.2', 24)
net.start()
net.pingAll()
net.stop()
~~~



5.  除了可以通过Python脚本创建基本的拓扑以外，还能在此基础上对性能进行限制。观察下面给出的脚本文件，addHost()语法可以对主机cpu进行设置，以百分数的形式；addLink()语法可以设置带宽bw、延迟delay、最大队列的大小  

~~~python
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
net = Mininet(host=CPULimitedHost, link=TCLink)
c0 = net.addController()
s0 = net.addSwitch('s0')
h0 = net.addHost('h0')
h1 = net.addHost('h1', cpu=0.5)
h2 = net.addHost('h1', cpu=0.5)
net.addLink(s0, h0, bw=10, delay='5ms',
max_queue_size=1000, loss=10, use_htb=True)
net.addLink(s0, h1)
net.addLink(s0, h2)
net.start()
net.pingAll()
net.stop()
~~~



##### 通过MiniEdit 工具画出拓扑图然后保存为.py文件

~~~python
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController  
from mininet.node import CPULimitedHost, Host, Node                              
from mininet.node import OVSKernelSwitch, UserSwitch   
from mininet.node import IVSSwitch    
from mininet.cli import CLI   
from mininet.log import setLogLevel, info                              
from mininet.link import TCLink, Intf
from subprocess import call                                                     

def myNetwork():
    
	net = Mininet( topo=None,    
		build=False,
		ipBase='10.0.0.0/8')                    
	
    info( '*** Adding controller\n' )                      
	c0=net.addController(name='c0',                     
		controller=Controller,        
		protocol='tcp',       
		port=6633)    
	
    info('*** Add switches\n')                    
	s2 = net.addSwitch('s2', cls=OVSKernelSwitch)                     
	s1 = net.addSwitch('s1', cls=OVSKernelSwitch)                     

    info( '*** Add hosts\n')
	h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
	h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)

    info( '*** Add links\n')                    
	net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s2, h3)
    net.addLink(s2, h4)                     
	
    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')                     
for controller in net.controllers:
    controller.start()
    
info( '*** Starting switches\n') 
net.get('s2').start([c0])                                                                                              
~~~