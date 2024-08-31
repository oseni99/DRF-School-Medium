#!/usr/bin/env bash

countdown(){
    declare desc="A simple countdown."

    local seconds="${1}"

    local end_time=$(($(date +%s) + seconds))

    while [ "$end_time" -ge "$(date +%s)" ]; do
        echo -ne "$(date -u --date @$(($end_time - $(date +%s))) +%H:%M:%S)\r"
        sleep 0.1
    done
}










