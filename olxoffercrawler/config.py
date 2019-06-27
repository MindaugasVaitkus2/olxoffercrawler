import re

def is_url(url):
    return re.match("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", url)

def read_urls(filename): 
    urls = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if is_url(line):
                urls.append(line)
            else:
                print(line, "is not a valid URL!")

    return urls
