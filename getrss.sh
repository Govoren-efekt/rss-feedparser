#!/bin/bash

curl -s -X POST -F "url=${1}"  https://getrssfeed.com | \
 grep window.location.replace | \
 cut -d'"' -f2 | \
 xargs -n 1 curl -s | \
 xidel -s --extract "//a[text()='RSS Feed']/@href" - | xargs ./rsstosql.py
