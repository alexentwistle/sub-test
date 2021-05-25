# SubTest
Identify a website's accessible and indexable subdomains

1. Take user input for the domain to be tested
2. Enumerate subdomains (using sublist3r) and export
3. Construct URLs from subdomains (include both HTTP and HTTPS versions if necessary)
4. Retrieve status codes for exported subdomains, using Requests library
5. Identify accessible subdomains, and check for indexability (look for 'noindex' tag in code)


## ToDo
- Tidy up output file (try TXT file instead of CSV)
- Prepend HTTP and/or HTTPS to the exported URLs and save as URL list.
- Use Requests library to retrieve status codes for URL list
- Check for noindex tag on accessible URLs


## Done
- Create requirements file for Sublist3r (and Requests library)
- Export Sublist3r result as CSV
