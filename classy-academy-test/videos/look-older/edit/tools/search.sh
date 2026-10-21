#!/bin/bash
# search.sh tag="query" [tag2="query2" ...]   (add --images to show photo pins too) -> pin/<tag>.json + pin/sheet_<tag>.jpg
cd "$(dirname "$0")/.." && PINDIR=$PWD/pin python3 -I tools/pin_search.py "$@"
