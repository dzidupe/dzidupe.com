#!/bin/bash

# Find the folder where this script effectively lives
PROJECT_ROOT=$(dirname "$(realpath "$0")")

cd "$PROJECT_ROOT"

#Run the watcher
while inotifywait -q -e close_write,create,delete reviews/; do
    python3 build.py
done