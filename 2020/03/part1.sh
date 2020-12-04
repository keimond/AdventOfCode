#!/bin/bash

# Sled path
X=3
Y=1

# Starting grid size
startX=$(head -1 input|egrep -o .|wc -l)
startY=$(cat input|wc -l)

# How many times should our grid repeat to the right so we have enough rows to make it to the bottom

hopsY=$(echo "${startY} / ${Y} + 1" | bc)

hopsX=$(echo "${hopsY} * ${X}" | bc)

repeat=$(echo "${hopsX} / ${startX} + 1" | bc)

gridX=$(echo "$repeat * $startX" | bc)

echo "Grid = ${gridX} x ${startY}"

declare -A array
cY=1
while read -r line; do
    cX=1
    for r in $(seq 1 $repeat); do
        for char in $(echo $line | egrep -o .); do
            array[${cX},${cY}]=${char}
            cX=$((cX+1))
        done
    done
    cY=$((cY+1))
done < input

echo "Starting the slide"

cX=1
cY=1
count=0
for slopes in $(seq 1 ${hopsY}); do
    cX=$((cX+X))
    cY=$((cY+Y))
    echo "${cX},${cY}"
    if [[ "${array[$cX,$cY]}" == "#" ]]; then
        count=$((count+1))
    fi
done

echo $count
