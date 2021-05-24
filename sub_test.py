import sublist3r

# Uncomment below to allow users to specify their own domain
# domain = input("Specify the domain: ")

# Placeholder. TODO: Remove
domain = "example.com"
subdomains = sublist3r.main(domain, 40, 'discovered_subdomains.csv', ports= None, silent=False, verbose= False, enable_bruteforce= False, engines=None)
