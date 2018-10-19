#!/bin/bash

echo -e "\033[0;36mBEGINNING FILE CLEAN\033[0m"
echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
sleep 2
while true
do
    if [ -d ./csv ]
    then
        rm ./csv/*
        echo -e "\033[0;35mINITIALIZING FILE SEARCH\033[0m"
        sleep 1.5

        echo -e "\033[0;33mCSV FILE SEARCH\033[0m"
        echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"

        if [ /*.csv ]
        then
            echo -e "CSV File Detected:\n"
            sleep 2
            ls ./*.csv
            sleep 3
            echo -e "Moving CSV Files to CSV Directory..\n"
            mv ./*.csv ./csv
            echo -e "Files Successfully moved!\n"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        else
            echo -e "No CSV Files Were Found!\n"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        fi
        break

    else
        mkdir csv
        echo -e "\033[0;31mDIRECTORY CREATED\033[0m"
        echo -e "\033[0;35mINITIALIZING FILE SEARCH\033[0m"
        sleep 1.5
    
        echo -e "\033[0;33mCSV FILE SEARCH\033[0m"
        echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"

        if [ /*.csv ]
        then
            echo -e "CSV File Detected:\n"
            sleep 2
            ls ./*.csv
            sleep 3
            echo -e "Moving CSV Files to CSV Directory..\n"
            mv ./*.csv ./csv
            echo -e "Files Successfully moved!"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        else
            echo -e "No CSV Files Were Found!"
            echo -e "\033[0;33m----------------------------------------------------------------------------------------------------------------\033[0m"
        fi
        break
    fi
done