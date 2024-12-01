#!/bin/bash

# Check if a directory name is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <directory_name>"
  exit 1
fi

# Check if the directory exists
if [ ! -d "$1" ]; then
  echo "Directory not found!"
  exit 1
fi

# Define the input file and Python script paths
PYTHON_SCRIPT="$1/$(basename $1).py"

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "Python script not found!"
  exit 1
fi

# Activate the Python virtual environment
source venv/Scripts/activate

# Run the Python script with the input file
python "$PYTHON_SCRIPT"

# Deactivate the Python virtual environment
deactivate