#!/usr/bin/python

'Indoor network before fire'

import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(args):

    net = Mininet_wifi()

    info("*** Creating nodes\n")
    ap2 = net.addAccessPoint('ap2', ssid='ssid_2', mode='g', channel='2', failMode="standalone",
                             mac='00:00:00:00:00:02', position='35,20,0', range=42)
    ap3 = net.addAccessPoint('ap3', ssid='ssid_3', mode='g', channel='3', failMode="standalone",
                             mac='00:00:00:00:00:03', position='65,45,0', range=30)
    ap4 = net.addAccessPoint('ap4', ssid='ssid_4', mode='g', channel='4', failMode="standalone",
                             mac='00:00:00:00:00:04', position='95,30,0', range=45)
    s5 = net.addSwitch('s5')
    h1 = net.addHost('h1', ip='10.0.0.1/8')
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:05', ip='10.0.0.2/8', position='5,45,0')
    c0 = net.addController('c0')

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    net.addLink(ap2, s5)
    net.addLink(ap3, s5)
    net.addLink(ap4, s5)
    net.addLink(s5, h1)

    if '-p' not in args:
        net.plotGraph(max_x=100, max_y=50)

    info("*** Starting network\n")
    net.build()
    c0.start()
    ap2.start([c0])
    ap3.start([c0])
    ap4.start([c0])
    s5.start([c0])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
