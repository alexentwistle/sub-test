# CHANGES

- accepts multiple domains as command line arguments and processes them all
- outputs results to console as well as files
- cleaned_subdomains file removed
- results now go into subdirectory, e.g. data/example.com/discovered_subdomains.txt
- redirect URL chain now recorded
- fixed bug (?) where the eventual response code was output next to a redirecting URL
  - e.g. your output was:
  - http://redirecting-url.com/ 200 History: <Redirect ...>
  - when in fact the first response from redirecting-url.com was 3xx 
  - not sure if this was your intention. now the final status code is at the end of the line of redirects
- added .gitignore file containing data/ which instructs git not to commit anything under data/
  - it is a good idea not to have subdomain enumeration results in your public github repo

Notes:
- It is now large enough to break up into functions
- I left sub_test.py "procedural" - i.e. flat, without functions, just executes top to bottom
- I wanted to show you how I would structure it with functions as well, check out sub_test_with_functions.py
