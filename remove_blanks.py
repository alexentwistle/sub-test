with open('discovered.txt') as infile, open('fixed.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # Skip empty lines
        outfile.write("http://" + line)  # Write non-empty lines to output. Once with HTTP protocol...
        outfile.write("https://" + line) # ... and once with HTTPS protocol