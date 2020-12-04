#!/bin/bash

# Sled path
X=3
Y=1

# Starting grid size
startX=$(head -1 input|egrep -o .|wc -l)
startY=$(cat input|wc -l)

# How many times should our grid repeat to the right so we have enough rows to make it to the bottom

echo "Grid = ${startX} x ${startY}"

declare -A array
cY=1
while read -r line; do
    cX=1
    for r in $(seq 1 ${startX}); do
        for char in $(echo ${line} | egrep -o .); do
            array[${cX},${cY}]=${char}
            cX=$((cX+1))
        done
    done
    echo "Row ${cY} done..."
    cY=$((cY+1))
done < input

echo;echo "Starting the slide"

cX=1
cY=1
count=0
for slopes in $(seq 1 ${hopsY}); do
    cX=$((cX+X))
    cY=$((cY+Y))
    # wrap
    if [ ${cX} -gt ${startX} ]; then
        cX=$((startX-cX))
    fi
    if [[ "${array[$cX,$cY]}" == "#" ]]; then
        echo "${cX},${cY}"
        count=$((count+1))
    fi
done

echo $count
