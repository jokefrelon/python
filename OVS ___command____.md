# 1. VXLAN简介

VXLAN 是 Virtual eXtensible LANs 的缩写，它是对 VLAN 的一个扩展，是非常新的一个 tunnel 技术，在Open vSwitch中应用也非常多。Linux 内核的 upstream 中也刚刚加入 VXLAN 的实现。相比 GRE tunnel 它有着很好的扩展性，同时解决了很多其它问题。

从数量上讲，它把 12 bit 的 VLAN tag 扩展成了 24 bit。从实现上讲，它是 L2 over UDP，它利用了UDP 同时也是 IPv4 的单播和多播，可以跨 L3 边界，很巧妙地解决了 GRE tunnel 和 VLAN 存在的不足，让组网变得更加灵活。

# 2. 实验环境

Linux内核模块在支持Open vSwitch之后又加入了支持隧道的功能，但是某些内核版本的的Linux可能只支持Open vSwitch而不支持隧道技术。支持隧道技术的对应最低Linux内核版本如下：

[![隧道技术支持内核版本协议](https://img1.sdnlab.com/wp-content/uploads/2014/12/%E9%9A%A7%E9%81%93%E6%8A%80%E6%9C%AF%E6%94%AF%E6%8C%81%E5%86%85%E6%A0%B8%E7%89%88%E6%9C%AC%E5%8D%8F%E8%AE%AE.png)](https://img1.sdnlab.com/wp-content/uploads/2014/12/隧道技术支持内核版本协议.png)

本实验操作系统是在两台虚拟机中安装的基于3.13Linux内核版本的Ubuntu 14.04.1，满足VXLAN正常运行的条件。同时需要安装好Open vSwitch，本实验安装的是Open vSwitch 2.3.0版本，具体安装步骤详见[《Open vSwitch2.3.0版本安装部署及基本操作》](https://www.sdnlab.com/3166)。

# 3. 基于Open vSwitch的VxLAN隧道搭建

本实验创建两台虚拟机并启动OpenvSwitch服务，最后创建VXLAN隧道并进行验证。实验中用到的网络拓扑如下：

[![隧道网络拓扑搭建](https://img1.sdnlab.com/wp-content/uploads/2014/12/%E9%9A%A7%E9%81%93%E7%BD%91%E7%BB%9C%E6%8B%93%E6%89%91%E6%90%AD%E5%BB%BA.png)](https://img1.sdnlab.com/wp-content/uploads/2014/12/隧道网络拓扑搭建.png)

*注：因为实验本身就是在虚拟环境下操作，所以实验中br1桥上实际上并没有再下挂任何主机，实验中我们是分别给两台虚拟机的br1指定两个不同网段的ip，然后通过搭建VXLAN隧道让这两个不同网段的网桥能够实现通信。*

## 3.1 配置Host1

启动好OVS服务后，我们先配置一下Host1。

在Host1上添加名为br0和br1的两个网桥：

~~~shell
 # ovs-vsctl add-br br0
 # ovs-vsctl add-br br1 
~~~





在br0上添加一个端口，将eth0挂载到br0上。这样做的目的是方便我们在虚拟网桥上添加多个端口供我们使用，这样不必受限于eth0的有限端口。



~~~shell
# ovs-vsctl add-port br0 eth0 
~~~
此时我们将原先eth0分配的ip清除并指定给br0，让虚拟机网络能通过br0继续工作。



~~~shell
# ifconfig eth0 0 up && ifconfig br0 192.168.146.131/24 up
~~~

根据实际情况配置一下br0的网关。



~~~shell
# route add default gw 192.168.146.2 br0
~~~

给br1网桥分配一个ip。



~~~shell
# ifconfig br1 10.0.0.1/24 up
~~~



## 3.2 配置Host2

按Host1同样步骤来配置Host2。



~~~shell
# ovs-vsctl add-br br0# ovs-vsctl add-br br1
# ovs-vsctl add-port br0 eth0# ifconfig eth0 0 up && ifconfig br0 192.168.146.136/24 up
# route add default gw 192.168.146.2 br0
~~~

给Host2的br1网桥分配一个和Host1中br1不同网段的ip。



~~~shell
# ifconfig br1 10.0.1.1/24 up
~~~



## 3.3 搭建VXLAN隧道

在搭建隧道之前我们先测试一下两台虚拟机Host1和Host2上的br0和br1两两之间是否能相互通信。



~~~shell
root@ubuntu:~# ping 192.168.146.136    ## Host1 ping Host2的br0
PING 192.168.146.136 (192.168.146.136) 56(84) bytes of data.64 bytes 
from 192.168.146.136: icmp_seq=1 ttl=64 time=1.88 ms64 bytes 
from 192.168.146.136: icmp_seq=2 ttl=64 time=0.703 ms……
~~~





~~~shell
root@ubuntu:~# ping 10.0.1.1    ## Host1 ping Host2的br1
PING 192.168.146.136 (192.168.146.136) 56(84) bytes of data. ……
~~~

br1和另一方的br1则不能通信，我们搭建隧道的目的就是让两台机器的br1(数据层面)能够实现通信。

\1. 在Host1上设置VXLAN，远端ip设置为Host2能对外通信的br0的ip。



~~~shell
# ovs-vsctl add-port br1 vx1 -- set interface vx1 type=vxlan options:remote_ip=192.168.146.136
~~~

[![vxlan在ovs中查看](https://img1.sdnlab.com/wp-content/uploads/2014/12/vxlan%E5%9C%A8ovs%E4%B8%AD%E6%9F%A5%E7%9C%8B.png)](https://img1.sdnlab.com/wp-content/uploads/2014/12/vxlan在ovs中查看.png)

\2. 在Host2上设置VXLAN，远端ip设置为Host1能对外通信的br0的ip。



~~~shell
# ovs-vsctl add-port br1 vx1 -- set interface vx1 type=vxlan options:remote_ip=192.168.146.131
~~~



## [![vxlan在ovs中查看131](https://img1.sdnlab.com/wp-content/uploads/2014/12/vxlan%E5%9C%A8ovs%E4%B8%AD%E6%9F%A5%E7%9C%8B131.png)](https://img1.sdnlab.com/wp-content/uploads/2014/12/vxlan在ovs中查看131.png) 3.4 验证VxLAN隧道

两台机器的br1互ping可以实现正常通信：



~~~
root@ubuntu:~# ping 10.0.1.1
PING 10.0.1.1 (10.0.1.1) 56(84) bytes of data.64 bytes 
from 10.0.1.1: icmp_seq=1 ttl=64 time=15.4 ms64 bytes 
from 10.0.1.1: icmp_seq=2 ttl=64 time=0.715 ms…… 

root@ubuntu:~# ping 10.0.1.1
PING 10.0.1.1 (10.0.1.1) 56(84) bytes of data.64 bytes 
from 10.0.1.1: icmp_seq=1 ttl=64 time=15.4 ms64 bytes 
from 10.0.1.1: icmp_seq=2 ttl=64 time=0.715 ms……
~~~

同时通过抓包证明数据包的使用协议的确是VXLAN，具体见下图：

[![vxlan通过wireshark抓包查看](https://img1.sdnlab.com/wp-content/uploads/2014/12/vxlan%E9%80%9A%E8%BF%87wireshark%E6%8A%93%E5%8C%85%E6%9F%A5%E7%9C%8B.png)](https://img1.sdnlab.com/wp-content/uploads/2014/12/vxlan通过wireshark抓包查看.png)

# 4. 结论

本实验搭建了基于Open vSwitch的VXLAN隧道，实现了不同网段内网机器的通信。实验是基于Open vSwitch的虚拟交换机进行实验的，有条件的朋友可以在真实环境中实验一下。