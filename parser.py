import paramiko
import re


def main():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('152.46.19.108', port=22, username='agupta38', password='narabhanc_85')
    stdin, stdout, stderr = ssh.exec_command('ifconfig')
    output = stdout.readlines()
    outputStr = ''
    for lines in output:
        outputStr = outputStr+lines
    length = len(output)
    # print(outputStr)
    info = []

    # Parsing IP Address
    ipaddr = re.findall("inet [.0-9]+", outputStr)

    ipaddrStr = ' '
    for i in ipaddr:
        ipaddrStr = ipaddrStr + i
    # print(ipaddrStr)

    ipaddr_final = re.findall("[0-9.]+", ipaddrStr)

    ipaddr_length = len(ipaddr_final)

    # print("length of IP address List: ", ipaddr_length)
    # for ifinal in ipaddr_final:
    #   print(ifinal)

    # print('Ip addresses : ',ipaddr_final)

    # Dictionary for IP Mapping
    ipMapping = {}

    for i in range (ipaddr_length):
        ipMapping[ipaddr_final[i]] = i
    # print(ipMapping)

    # Parsing MAC Address

    macaddress = re.findall("ether [0-9:a-f]+", outputStr)

    macAddrStr = ' '
    for m in macaddress:
        macAddrStr = macAddrStr + m + ' '
    # print(macAddrStr)

    macaddr_final = re.findall("0[0-9:a-f]+", macAddrStr)
    # For loopback Address
    macaddr_final.append("lo")

    # for mfinal in macaddr_final:
    # print(mfinal)

    macaddr_length = len(macaddr_final)

    # Dictionary for Mac Mapping
    macMapping = {}

    for i in range(macaddr_length):
        macMapping[macaddr_final[i]] = i
    # print(macMapping)

    # Parsing Interfaces

    interface_tmp = re.findall("eth[0-9]", outputStr)
    linterface = re.findall("lo{1}", outputStr)
    # print("tmp_inter",interface_tmp)
    # print("linterfaace : ",linterface)
    interface = interface_tmp+linterface
    # print("Interfaces are : ",interface)
    interface_length = len(interface)

    # Dictionary for Interfaces Name
    interfaceMapping = {}

    for i in range(interface_length):
        interfaceMapping[interface[i]] = i
    # print(interfaceMapping)

    # Dictionary for Interface Type
    itypeMapping = {}
    for i in range(interface_length):
        # if interface[i][:3] == 'eth0' or interface[i] == 'eth1':
        if interface[i][:3] == 'eth':
            itypeMapping[interface[i]] = 'Ethernet'
        elif interface[i] == 'lo':
            itypeMapping[interface[i]] = 'LoopBack'
        else:
            itypeMapping[interface[i]] = 'Misc'

    # print("Interface Type Dic : ", itypeMapping)

    # print("Following Mac address are configured in this machine")

    while True:

        choice = int(input("How do you like to display info\n 1. Using IP Address 2.Using Mac Address 0. To quit\n" ))

        if choice == 1:
            print("Following IP address are configured in this machine")
            for i in ipaddr_final:
                print(i)

            ip = input("Please Entered the desired IP Address \n")
            print("IP Address : ", ipaddr_final[ipMapping.get(ip)])
            print("Mac Address : ", macaddr_final[ipMapping.get(ip)])
            print("Interface Name : ", interface[ipMapping.get(ip)])
            print("Interface Type: ", itypeMapping[interface[ipMapping.get(ip)]])

        if choice == 2:
            print("Following Mac address are configured in this machine")
            for m in macaddr_final:
                print(m)

            mac = input("Please Entered the desired Mac Address \n")
            # print("Error : ", macMapping.get(mac))
            print("IP Address : ", ipaddr_final[macMapping.get(mac)])
            print("Mac Address : ", macaddr_final[macMapping.get(mac)])
            print("Interfac Name : ", interface[macMapping.get(mac)])
            print("Interface Type: ", itypeMapping[interface[macMapping.get(mac)]])

        if choice == 100:
            print("Following Inteface types/names  are configured in this machine")
            for i in interface:
                print("Interface Name : ", i, "      |      Interface Type : ", itypeMapping[i])

            mac = input("Please Entered the desired Mac Address \n")
            # print("Error : ", macMapping.get(mac))
            print("IP Address : ", ipaddr_final[macMapping.get(mac)])
            print("Mac Address : ", macaddr_final[macMapping.get(mac)])
            print("Interfac Name : ", interface[macMapping.get(mac)])
            print("Interface Type: ", itypeMapping[interface[ipMapping.get(ip)]])

        if choice == 0:
            break




main()