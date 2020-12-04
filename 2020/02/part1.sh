#!/bin/bash

count=0

while read pol alpha pass; do
  pol1=$( echo ${pol} | cut -d- -f1 )
  pol2=$( echo ${pol} | cut -d- -f2 )
  char=$( echo ${alpha} | cut -d: -f1 )
  nappear=$( echo ${pass} | egrep -o ${char} | sort | uniq -c | awk '{print $1}' )
  if [ ${pol1} -le ${nappear:-0} ] && [ ${pol2} -ge ${nappear:-0} ]; then
    count=$((${count}+1))
    echo $count
  fi
done < input

echo ${count}
