# Mininet 操作

### 常用命令简析

##### 拓扑建立

~~~shell
sudo mn --topo xxx
~~~



###### 树形拓扑

~~~shell
sudo mn --topo=tree,fanout=2,depth=2
~~~



###### 直线型拓扑

~~~shell
sudo mn --topo=linear,4
~~~



###### 单一型

~~~shell
sudo mn --topo =single,3
~~~



###### Python文件型

~~~shell
sudo mn --custom xxx.py --topo mytopo
~~~

##### 选择交换机

~~~shell
sudo mn --switch
~~~

--switcher 的参数主要有下面几个  **ovsk ovsbr ivs lxbr user**

前面三种均为OVS型交换机，后面两种分别为内核型(linux bridge)和用户型(user)交换机,其中内核型和OVS型的吞吐量比用户性大很多，因此一般采用后两种



##### 选择控制器

~~~shell
sudo mn --controller = remote
~~~

​      - **ip** = [控制器的IP地址]
​      - **port** = [控制器的端口号]
如果 **--ip** 和 **--port** 省略的话，则默认使用本地ip地址，端口默认使用**6653**或**6633**端口号。

##### 固定MAC地址

**--mac** 使用这个参数可以让MAC地址从小到达排列，使得复杂的网络更清晰，容易辨识各个组件的MAC地址。不使用这个参数的话，复杂的网络容易混乱。

<hr>

### 互交界面操作

##### 添加主机

~~~shell
py net.addHost('h3')
~~~



##### 添加Switch(非必须)

~~~shell
py net.addSwitch("s2")
~~~



##### 给 S1witch添加端口eth3 

~~~shell
py s1.attach('s1-eth3')
~~~



##### 把主机添加到Switch

~~~shell
py net.addLink(s1,net.get('h3'))
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
|	link [node id] [node id] up/down |	打开/关闭两个节点的链路|


