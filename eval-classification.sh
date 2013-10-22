#!/bin/bash

MODEL=$1
shift
TEST_DATA=$1
shift

join -o 1.1 -o 2.1 -1 2 -2 2 <(cat $TEST_DATA |sed 's/\([-0-9]\) [0-9.]*/\1/' | cut -f1 -d'|') <(cat $TEST_DATA | vw -i $MODEL --quiet -p /dev/stdout) | sed 's/^-1/0/' | perf $*
