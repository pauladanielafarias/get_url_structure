import json
from urllib.parse import urlparse , parse_qs, urlencode
import tldextract
#import tkinter as tk

url = input("Enter url:")

def getUrlStructure(url):
    
    urlParsed = urlparse(url)
    scheme = urlParsed.scheme
    netloc = urlParsed.netloc
    port=urlParsed.port
    path = urlParsed.path    
    query = urlParsed.query
    params = urlParsed.params
    fragment =urlParsed.fragment
    
    urlExtract =tldextract.extract(url)
    domain=urlExtract.domain
    subdomain = urlExtract.subdomain
    suffix = urlExtract.suffix
    
    queries = parse_qs(url)
    
    urlStructure={
        "entered url":url,
        "netloc":netloc,
        "scheme":scheme,
        "subdomain":subdomain,
        "domain": domain,
        "port": port,
        "suffix":suffix,
        "path":path,
        "parameters":params,
        "query":query,
        "queryParameters":queries,
        "fragment":fragment
    }
   
    
    # "x" will create a file, returns an error if the file exist
    #text_file = open("myUrlParams.txt", "x")
    #json_file = open("myUrlParams.json", "x")
    
    return print(json.dumps(urlStructure,indent=2))

    
getUrlStructure(url)   
    