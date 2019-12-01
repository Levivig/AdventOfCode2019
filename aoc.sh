#!/bin/bash


if [ "$1" = "--newday" ]; then
    currentDay="day$2"

    mkdir $currentDay
    mv ./.template/day.py ./$currentDay/"$currentDay.py"
    mv ./.template/input.txt ./$currentDay/input.txt
else
    currentDay="day$1"
    python $currentDay/"$currentDay.py"
fi