import sublist3r
import requests


domain = "global-savings-group.com" # Placeholder. TODO: Replace with user input (line 7)

#domain = input("Please enter your domain: ") # BUG: When this is used instead of line 5, the script ends after doing nothing.

subdomains = sublist3r.main(domain, 10, 'discovered_subdomains.txt', ports= None, silent=True, verbose= False, enable_bruteforce= False, engines=None)

with open('discovered_subdomains.txt') as infile, open('cleaned_subdomains.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # Skip empty lines generated by Sublist3r
        outfile.write("http://" + line)  # Write non-empty lines to output. Once with HTTP protocol...
        outfile.write("https://" + line) # ... and once with HTTPS protocol

with open('cleaned_subdomains.txt') as infile, open('subdomain_responses.txt', 'w') as outfile:
    for url in infile:
        try:
            clean_url = url.rstrip()
            r = requests.get(clean_url, timeout=5)
#           r = requests.get(clean_url, headers={'Connection': 'close'})
#           r.encoding = 'utf-8'
            outfile.write(clean_url+": "+str(r.status_code)+". History: "+str(r.history)+"\n")
        except requests.ConnectionError as e:
            outfile.write(clean_url+": Connection Error."+"\n")
