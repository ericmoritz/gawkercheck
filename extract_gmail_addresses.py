#!/usr/bin/python
import hashlib
import csv
import sys

reader = csv.reader(sys.stdin)

# Pop off the header
r = reader.next()

emails = {}
for r in reader:
    for v in map(str.strip, [r[28], r[39]]):
        if v:
            print v

