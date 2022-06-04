#!/bin/sh

set -e

python3 ./fof.py "$(tput cols)" "$(tput lines)" "$(whoami)" "$(which sudo)" "$(which pkexec)"
