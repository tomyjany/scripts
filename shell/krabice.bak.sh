#!/bin/bash
i=0
while [ $i -lt $1 ]
do
	j=0
	while [ $j -lt $2 ]
	do
		pravdepodobnost=$(($RANDOM % $1))
		if [ $i -eq 0 ] || [ $i -eq $(($1-1)) ]
		then
			if [ $j -eq 0 ] ||  [ $j -eq $(($2-1)) ]
			then
				tisk="."
			else
				tisk="-"
			fi
		else
			if [ $j -eq 0 ] || [ $j -eq $(($2-1)) ]
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
