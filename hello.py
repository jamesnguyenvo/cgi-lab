#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
from urllib.parse import parse-qs

import json
import os

print("Content-Type: text/html\n")
print()
print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
print("<head>")
print("<title>Hello</title>")
print("<style>pre {wite-space: pre-wrap; word-wrap: break-word;}</style>/")
print("</head>")
print("<h2>Hello World</h2>")
# cgi.print_environ()
# print(os.environ)

# Print Query String
qs = os.environ.get("QUERY_STRING", None)
print("<dl>")
print("<dt>QUERY_STRING</dt>")
print("<dd>{}</dd>".format(parse_qs(qs)))
ua = os.environ.get("HTTP_USER_AGENT", None)
print("<dd>{}</dd>") #missing some stuff 
print("</dl>")

# Dump environment variables
print("<pre>")
print(json.dumps(dict(os.environ), indent=4))
print("</pre>")