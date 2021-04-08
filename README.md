# SubTest
Identify a website's accessible and indexable subdomains

1. Take user input for the domain to be tested
2. Enumerate subdomains (using sublist3r) and export
3. Retrieve status codes for exported subdomains, using Requests library
4. Identify accessible subdomains, and check for indexability (look for 'noindex' tag in code)


