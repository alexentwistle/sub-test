import sublist3r

# Uncomment below to allow users to specify their own domain
# domain = input("Specify the domain: ")

# Placeholder. TODO: Remove
domain = "example.org"
subdomains = sublist3r.main(domain, 40, 'discovered.txt', ports= None, silent=True, verbose= False, enable_bruteforce= False, engines=None)

with open('discovered.txt') as infile, open('fixed.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # Skip empty lines
        outfile.write("http://" + line)  # Write non-empty lines to output. Once with HTTP protocol...
        outfile.write("https://" + line) # ... and once with HTTPS protocol