#!/bin/bash
i=0
while [ $i -lt $2 ]
do
	j=0
	while [ $j -lt $1 ]
	do
		pravdepodobnost=$(($RANDOM % $2))
		if [ $i -eq 0 ] || [ $i -eq $(($2-1)) ]
		then
			if [ $j -eq 0 ] ||  [ $j -eq $(($1-1)) ]
			then
				tisk="."
			else
				tisk="-"
			fi
		else
			if [ $j -eq 0 ] || [ $j -eq $(($1-1)) ]
			then
				tisk="|"
			else
				if [ $pravdepodobnost -lt $i ]
				then
					tisk="O"
				else
					tisk=" "
				fi
			fi
		fi
		echo -n "$tisk"
		let j++
	done
	echo
	let i++
done
