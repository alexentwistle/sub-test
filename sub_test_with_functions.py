import sublist3r
import requests
import os
import sys
import traceback

# the other script is fine but as things get more complex
# it is better to isolate specific tasks into functions

# start reading it at the bottom

def get_domains_from_argv():
    # sys.argv is a list of the command line arguments
    # the first element is the script name, e.g. sub_test.py
    # refuse to run without at least one domain
    if len(sys.argv) < 2:
        print("Error: expected domain(s), e.g.:")
        print("python", sys.argv[0], "example.com anotherexample.com")
        exit(1)

    # discard first element (script name) - the rest are our domains
    domains = sys.argv[1:]
    return domains

def create_data_dir(domain):
    # first check that data dir exists
    if not os.path.isdir("data"):
        # if not, create it
        os.mkdir(os.path.join("data"))
    # use path.join to use correct path separator per OS: \ for windows and / for normal OSes
    data_dir = os.path.join("data", domain)
    # create data/$domain subdirectory
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
    else:
        # warn that we are probably overwriting data
        print("Warning: data directory", data_dir, "already exists")
    return data_dir

def discover_subdomains(domain, data_dir):
    print("Running sublist3r for:", domain)
    # path to sublister file. anything that is repeated goes into a variable, we don't like to repeat ourselves
    sublist3r_file = os.path.join(data_dir, 'discovered_subdomains.txt')
    # get subdomains
    sublist3r.main(domain, 10,sublist3r_file, ports= None, silent=True, verbose= False, enable_bruteforce= False, engines=None)

    domains = [domain] # now includes base domain 
    # get subdomains from file
    with open(sublist3r_file) as infile:
        for line in infile:
            # Skip empty lines generated by Sublist3r
            if not line.strip():
                continue
            domains.append(line.rstrip())

    print("Discovered subdomains:", " ".join(domains))
    print("Discovered subdomains saved to:", sublist3r_file)
    return domains

# creates http and https URLs for each subdomain passed
def create_url_list_from_subdomains(subdomains):
    # start with the base domains http and https URLs
    urls = []
    for subdomain in subdomains:
        # temp code, remove
        # exceptions "escape" their functions "up the stack" (to the calling function)
        # until they find a except: block
        # otherwise execution halts
        # this is handled in main() except: block
        if subdomain == "summer.bitsios.com":
            # this is how you raise/"throw" an exception BTW
            raise Exception("Don't with fuck Summer")
        urls.append("http://" + subdomain + "/")
        urls.append("https://" + subdomain + "/")
    return urls

# make request module's response object into string of url + status code
def stringify_response(response):
    return response.url + " " + str(response.status_code)

# request URLs and report status code and redirect chains
def request_urls(urls, data_dir):
    subdomain_responses_file = os.path.join(data_dir, 'subdomain_responses.txt')
    with open(subdomain_responses_file, 'w') as outfile:
        # request each URL and output status code and redirect chains
        for url in urls:
            try:
                # simulate unexpected errors
                # will be handled by 'except Exception as e:' block in this function
                # for exception handling demonstration purposes
                if url == "http://stefania.fokaeos.com/":
                    # let's trigger a str + int exception
                    tasinet = "tas" + 1 + "net"

                response = requests.get(url, timeout=5)
                # record all redirect urls and status codes into a list
                redirect_chain = []
                if len(response.history) > 0:
                    for history in response.history:
                        # made stringify_response into a function since it is used twice
                        # arguably this is overkill
                        redirect_chain.append(stringify_response(history))
                # final destination
                redirect_chain.append(stringify_response(response))
                # make redirect_chain list into a string joined with " -> "
                # (if redirect_chain only has one item, no " -> " is inserted)
                outline = " -> ".join(redirect_chain)
                # print(to console and write to file
                print(outline)
                outfile.write(outline+"\n")
            # this block handles all Requests related exceptions
            # these are expected errors
            except requests.exceptions.RequestException as e:
                errline = url + " Connection Error: " + str(e)
                print(errline)
                outfile.write(errline +"\n")
            # if other shit goes wrong we still want to continue processing
            # other subdomains will continue processing
            except Exception as e:
                errline = url + " UNEXPECTED ERROR: " + str(e)
                print(errline)
                # this prints a "stack traceback" 
                # so you get nice error line numbers
                # must-have but not needed in the file so we just print to console
                # https://stackoverflow.com/questions/3702675/how-to-catch-and-print-the-full-exception-traceback-without-halting-exiting-the
                # https://docs.python.org/3/library/traceback.html
                print(traceback.format_exc())
                outfile.write(errline +"\n")

    print("Subdomain responses saved to:", subdomain_responses_file)

# main body
def main():
    # get domains from command line arguments or exit if none passed
    domains = get_domains_from_argv()
    # enumerate each domain
    for domain in domains:
        try:
            # create data dir.
            # we do this here because we need it both in discover_subdomains and request_urls
            # so we pass it into both as a function argument
            data_dir = create_data_dir(domain)
            # simulate something unexpected going wrong
            # this is the "same" as the exception for summer.bitsios.com
            # in create_url_list_from_subdomains
            # i.e. will be handled by except: block below
            if domain == "ds.tasinet.gr":
                raise Exception("Booby trapped!")
            # get subdomains from sublisted. now includes base domain as well.
            subdomains = discover_subdomains(domain, data_dir)
            urls = create_url_list_from_subdomains(subdomains)
            request_urls(urls, data_dir)
        # catch generic exceptions so we can continue with other domains if something unexpected goes wrong
        except Exception as e:
            print("Unexpected error handling", domain+':', e)
            print(traceback.format_exc())
        # this block executes whether an exception was thrown or not
        finally:
            print("  ---- ")

main()
