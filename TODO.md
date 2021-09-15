[✓] remove exception handling demo code
- delete sub_test.py since you are comfortable with functions (and rename the sub_test__with_functions file)

To think about:
- reuse discovered_subdomains file if it exists?
- How to handle SSL certificate errors? Currently they are shown as 503
  - You can ignore them https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
- Show some kind of page signature to indicate similar pages? 
  - page title and first h1 title?
  - ETAG HTTP Response header when present?
  - hash of response body? MD5 or something
- Output file to CSV?
- check indexability of pages:
  - meta noindex tag? (need html parsing)
  - X-Robot-tag? (you can already find this if you find the response headers from request's response object)
  - robots.txt? + warning if there is both this and next-gen robots tags (header or meta tag)
- Extract SEO content from page? (need html parsing)
  - <title>
  - <link rel="canonical">
  - <h1>

