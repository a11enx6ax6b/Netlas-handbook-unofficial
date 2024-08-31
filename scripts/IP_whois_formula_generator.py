import ipaddress
import sys
# Generates filter based on your provided file containing IP for IP Whois lookup
# python script.py {file_name_containing_IP}
# Sample output: ip:(8.8.4.0 OR 8.8.8.0 OR 8.35.200.0 OR 34.0.233.0 OR 34.0.235.0 )
netlas_query=""
with open(sys.argv[1],'r') as file:
    for ip in file:
        start_ip= ip.strip().split('/')[0]
        netlas_query=netlas_query+start_ip+" OR "
netlas_query=''.join(netlas_query.rsplit('OR ',1)[:-1])
print(f"ip:({netlas_query})")
