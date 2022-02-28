#!/usr/bin/python

'Outdoor network after fire'

import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(args):

    net = Mininet_wifi()

    info("*** Creating nodes\n")
    ap1 = net.addAccessPoint('ap1', ssid='ssid_1', mode='g', channel='1', failMode="standalone",
                             mac='00:00:00:00:00:01', position='500,1000,0', range=600)
    ap2 = net.addAccessPoint('ap2', ssid='ssid_2', mode='g', channel='2', failMode="standalone",
                             mac='00:00:00:00:00:02', position='400,300,0', range=650)
    ap4 = net.addAccessPoint('ap4', ssid='ssid_4', mode='g', channel='4', failMode="standalone",
                             mac='00:00:00:00:00:04', position='1400,500,0', range=650)
    ap5 = net.addAccessPoint('ap5', ssid='ssid_5', mode='g', channel='5', failMode="standalone",
                             mac='00:00:00:00:00:05', position='2050,300,0', range=450)
    ap6 = net.addAccessPoint('ap6', ssid='ssid_6', mode='g', channel='6', failMode="standalone",
                             mac='00:00:00:00:00:06', position='1950,800,0', range=450)
    ap7 = net.addAccessPoint('ap7', ssid='ssid_7', mode='g', channel='7', failMode="standalone",
                             mac='00:00:00:00:00:07', position='2900,750,0', range=550)
    s8 = net.addSwitch('s8')
    h1 = net.addHost('h1', ip='10.0.0.1/8')
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:08', ip='10.0.0.2/8', position='1000,100,0')
    c0 = net.addController('c0')

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    net.addLink(ap1, s8)
    net.addLink(ap2, s8)
    net.addLink(ap4, s8)
    net.addLink(ap5, s8)
    net.addLink(ap6, s8)
    net.addLink(ap7, s8)
    net.addLink(s8, h1)

    if '-p' not in args:
        net.plotGraph(max_x=3000, max_y=1200)

    info("*** Starting network\n")
    net.build()
    c0.start()
    ap1.start([c0])
    ap2.start([c0])
    ap4.start([c0])
    ap5.start([c0])
    ap6.start([c0])
    ap7.start([c0])
    s8.start([c0])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
