#!/usr/bin/python
import hashlib
import sys
import csv
from pprint import pprint
from itertools import imap

# Load in the gawker hashes
gawker_hashes = set(r[1] for r in csv.reader(open("./gawker.csv", "r")))


for email in imap(str.strip, sys.stdin):
    m = hashlib.md5()
    m.update(email)
    md5hash = m.hexdigest()
    if md5hash in gawker_hashes:
        print email
