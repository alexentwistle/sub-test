import requests
# import time

# Open fixed.txt
# For each URL in fixed.txt, run requests
# Return status code


#def check(url):
with open('fixed.txt') as infile, open('results.txt', 'w') as outfile:
    for url in infile:
        try:
            clean_url = url.rstrip()
            r = requests.get(clean_url, timeout=5)
#           r = requests.get(clean_url, headers={'Connection': 'close'})
#           r.encoding = 'utf-8'
            outfile.write(clean_url+": "+str(r.status_code)+"\n")
        except requests.ConnectionError as e:
            outfile.write(clean_url+": Connection Error."+"\n")