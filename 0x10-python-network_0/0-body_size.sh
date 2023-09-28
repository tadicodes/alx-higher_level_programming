#!/bin/bash
# send a request to URL with and displays the size of the response
curl -s "$1" | wc -c
