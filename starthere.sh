#!/bin/bash

# starthere.sh - Menu to run Python files in this repo

# Find all .py files in the current directory
PY_FILES=(*.py)

if [ ${#PY_FILES[@]} -eq 0 ]; then
    echo "No Python files found in this directory."
    exit 1
fi

echo "Select a Python file to run:"
select FILE in "${PY_FILES[@]}" "Quit"; do
    if [[ "$REPLY" -gt 0 && "$REPLY" -le "${#PY_FILES[@]}" ]]; then
        echo "Running $FILE..."
        python3 "$FILE"
        break
    elif [[ "$REPLY" -eq $((${#PY_FILES[@]}+1)) ]]; then
        echo "Exiting."
        break
    else
        echo "Invalid option. Try again."
    fi
done