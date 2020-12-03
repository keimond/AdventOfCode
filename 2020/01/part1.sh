#!/bin/bash

numbers=($(cat input))
found=0
pos1=0

for n1 in ${numbers[@]}; do
  if [ $found -eq 1 ]; then break; fi
  for n2 in ${numbers[@]}; do
    if [ $found -eq 1 ]; then break; fi
    if [ $((n1+n2)) -eq 2020 ]; then
      found=1
      echo "${n1} * ${n2} = $((n1*n2))"
    fi
  done
done
