#!/bin/bash

count=0

while read pol alpha pass; do
  pol1=$(($( echo ${pol} | cut -d- -f1 )-1))
  pol2=$(($( echo ${pol} | cut -d- -f2 )-1))
  char=$( echo ${alpha} | cut -d: -f1 )
  passwd=($(echo ${pass}| egrep -o .))
  if ( [[ "${passwd[${pol1}]}" == ${char} ]] && ! [[ "${passwd[${pol2}]}" == ${char} ]] ) ||
     ( [[ "${passwd[${pol2}]}" == ${char} ]] && ! [[ "${passwd[${pol1}]}" == ${char} ]] ); then
    count=$((${count}+1))
  fi
done < input

echo ${count}
