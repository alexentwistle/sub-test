import sublist3r
import requests


domain = "playretrogames.com" # Placeholder. TODO: Replace with user input

# domain = input("Please enter your domain: ") # When this is used instead, the command ends after doing nothing.

subdomains = sublist3r.main(domain, 40, 'discovered.txt', ports= None, silent=True, verbose= False, enable_bruteforce= False, engines=None)

with open('discovered.txt') as infile, open('fixed.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # Skip empty lines
        outfile.write("http://" + line)  # Write non-empty lines to output. Once with HTTP protocol...
        outfile.write("https://" + line) # ... and once with HTTPS protocol

with open('fixed.txt') as infile, open('results.txt', 'w') as outfile:
    for url in infile:
        try:
            clean_url = url.rstrip()
            r = requests.get(clean_url, timeout=5)
#           r = requests.get(clean_url, headers={'Connection': 'close'})
#           r.encoding = 'utf-8'
            outfile.write(clean_url+": "+str(r.status_code)+". History: "+str(r.history)+"\n")
        except requests.ConnectionError as e:
            outfile.write(clean_url+": Connection Error."+"\n")