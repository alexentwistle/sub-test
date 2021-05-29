# SubTest
Identify a website's accessible and indexable subdomains

1. Take user input for the domain to be tested
2. Enumerate subdomains (using sublist3r) and export
3. Construct URLs from subdomains (include both HTTP and HTTPS versions if necessary)
4. Retrieve status codes for exported subdomains, using Requests library
5. Identify accessible subdomains, and check for indexability (look for 'noindex' tag in code)


## ToDo
- Test responses for different status codes
- Add response history (i.e. redirect steps - currently, just the final step is being reported)
- Check for noindex tag on accessible URLs


## Done
- Create requirements file for Sublist3r (and Requests library)
- Created sub_test.py, which runs Sublist3r on example.org and outputs the subdomains as a txt file (stripped of blank lines)
- sub_test.py now prepends HTTP and HTTPS to each exported URL, and saves the new URL list as 'fixed.txt'
- Use Requests library to retrieve status codes for URL list
- Add exception handling for Connection Error


## Temporary workflow
1. sub_test.py 
- enumerates subdomains for domain (currently fixed, eventually will take user input)
- output as 'discovered.txt'. clean up URLs and prepend protocols, and output as 'fixed.txt'

2. check_status.py
- return status code for each URL in 'fixed.txt', and output results to 'results.txt'