import nmap

nm = nmap.PortScanner()

target = '***'
options = '-sP -sV -sC scan_results'

nm.scan(target, arguments=options)

for host, result in nm.all_hosts():
    print("Host: %s(%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    print(f'Open ports:')
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol].keys()
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))
            if state == 'open':
                print(f'Service: {nm[host][protocol][port]["service"]}')
                print(f'Version: {nm[host][protocol][port]["version"]}')
