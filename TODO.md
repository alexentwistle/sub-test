- remove exception handling demo code
- delete sub_test.py since you are comfortable with functions (and rename the sub_test__with_functions file)

To think about:
- reuse discovered_subdomains file if it exists?
- How to handle SSL certificate errors? Currently they are shown as 503
  - You can ignore them https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
- Show some kind of page signature to compare similar pages? 
  - ETAG HTTP Response header when present?
  - hash of response body? MD5 or something
- Output file to CSV?
