# SubTest
Identify a website's accessible and indexable subdomains

1. Receive user input for the domain to be tested (curretly using fixed placeholder)
2. Enumerate subdomains (using sublist3r) and export
3. Construct URLs from subdomains (include both HTTP and HTTPS versions if necessary)
4. Retrieve status codes for exported subdomains, using Requests library
5. Identify accessible subdomains, and check for indexability (look for 'noindex' tag in code)


## ToDo
- Add comma delimiters to 'sub_responses.txt' to enable conversion to csv / xlsx OR use pandas to make dataframe
- Add more detail to Reponse History (i.e. each URL of redirection step)
- Check HTML response for noindex tag on accessible URLs



## Done
- Create requirements file for Sublist3r (and Requests library)
- Created sub_test.py, which runs Sublist3r on example.org and outputs the subdomains as a txt file (stripped of blank lines)
- sub_test.py now prepends HTTP and HTTPS to each exported URL, and saves the new URL list as 'fixed.txt'
- Use Requests library to retrieve status codes for URL list
- Add exception handling for Connection Error
- Add response history for redirected URLs
- Test responses for different status codes (e.g.200,301,302,4xx, 500 have been succesful)



## Temporary workflow
1. sub_test.py 
- enumerates subdomains for domain (currently fixed, eventually will take user input)
- output as 'discovered_subdomains.txt'. clean up URLs and prepend protocols, and output as 'cleaned_subdomains.txt'
- return status code for each URL in 'cleaned_subdomains.txt', and output results to 'sub_responses.txt'

2. check_status.py
- removed: no longer needed