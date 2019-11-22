### 第一组 参数后面用 " = " 号

~~~shell
frelon@ubuntu:~$ sudo mn --custom=sdn-six.py --topo=mytopo --switch=ovsk,protocols=OpenFlow13 --controller=remote,ip=127.0.0.1,port=6633 --mac
[sudo] password for frelon:
*** Creating network
*** Adding controller
*** Adding hosts:
pc1 pc2 pc3 pc4
*** Adding switches:
sw1 sw2 sw3 sw4
*** Adding links:
(pc1, sw1) (pc2, sw1) (pc3, sw4) (pc4, sw4) (sw2, sw1) (sw2, sw4) (sw3, sw1) (sw3, sw4)
*** Configuring hosts
pc1 pc2 pc3 pc4
*** Starting controller
c0
*** Starting 4 switches
sw1 sw2 sw3 sw4 ...
*** Starting CLI:
mininet> pingall
*** Ping: testing ping reachability
pc1 -> pc2 pc3 pc4
pc2 -> pc1 pc3 pc4
pc3 -> pc1 pc2 pc4
pc4 -> pc1 pc2 pc3
*** Results: 0% dropped (12/12 received)
~~~



### 第一组 参数后面用 "   " 空白字符串

~~~shell
frelon@ubuntu:~$ sudo mn --custom sdn-six.py --topo mytopo --switch ovsk,protocols=Openflow13 --controller remote,ip=127.0.0.1,port=6633 --mac
*** Creating network
*** Adding controller
*** Adding hosts:
pc1 pc2 pc3 pc4
*** Adding switches:
sw1 sw2 sw3 sw4
*** Adding links:
(pc1, sw1) (pc2, sw1) (pc3, sw4) (pc4, sw4) (sw2, sw1) (sw2, sw4) (sw3, sw1) (sw3, sw4)
*** Configuring hosts
pc1 pc2 pc3 pc4
*** Starting controller
c0
*** Starting 4 switches
sw1 sw2 sw3 sw4 ...
*** Starting CLI:
mininet> pingall
*** Ping: testing ping reachability
pc1 -> X X X
pc2 -> X X X
pc3 -> X X X
pc4 -> X X X
*** Results: 100% dropped (0/12 received)
~~~



### 由上可知,最好不要省略 " = " 号