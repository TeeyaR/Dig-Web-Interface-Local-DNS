import dns.resolver

def dns_lookup(domain, nameserver):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [nameserver]
    
    records = []

    # Lookup CNAME record
    try:
        result = resolver.resolve(domain, 'CNAME')
        for cnameval in result:
            records.append((domain, 'CNAME', result.rrset.ttl, cnameval.to_text()))
    except dns.resolver.NoAnswer:
        records.append((domain, 'CNAME', 'N/A', 'No CNAME record found'))
    # Lookup A record
    try:
        result = resolver.resolve(domain, 'A')
        for ipval in result:
            records.append((domain, 'A', result.rrset.ttl, ipval.to_text()))
    except dns.resolver.NoAnswer:
        records.append((domain, 'A', 'N/A', 'No A record found'))
    
    # Lookup NS (Name Server) records
    try:
        result = resolver.resolve(domain, 'NS')
        for nsval in result:
            records.append((domain, 'NS', result.rrset.ttl, nsval.to_text()))
    except dns.resolver.NoAnswer:
        records.append((domain, 'NS', 'N/A', 'No NS record found'))

    # Print the results in the desired format
    print(f"{'Domain':<20} {'Type':<10} {'TTL':<10} {'Answer'}")
    print("="*60)
    for record in records:
        print(f"{record[0]:<20} {record[1]:<10} {record[2]:<10} {record[3]}")

# Prompt user for domain and nameserver input
domain = input("Enter the domain name: ")
nameserver = input("Enter your private DNS server IP: ")
dns_lookup(domain, nameserver)
