#!/usr/bin/env bash
set -eou pipefail 

for i in $(seq 1 966262); do
    w3m -dump -T text/html "http://bash.org/?$i"  > quotes/"$i".txt
    sleep(0.1)
done
