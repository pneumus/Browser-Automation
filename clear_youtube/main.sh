#!/bin/bash

# Infinite loop to keep restarting the Python script if it fails
while true
do
    # Execute the Python script
    python3 click_the_x.py

    # Check the exit status of the Python script
    if [ $? -ne 0 ]; then
        echo "Script crashed with exit code $?. Restarting ..."
    else
        echo "Script exited successfully. Restarting ..."
    fi

    # Optional: Add a sleep time to avoid overwhelming the system
    sleep 2
done

