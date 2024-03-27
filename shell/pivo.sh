#!/bin/bash
if [ $# -eq 0 ]
then
	echo "nezadal jsi vstupni argument"
	exit
elif [ 0 -gt $1  ] 
then
	echo "zadal jsi zaporny pocet piv"
	exit
elif [ $1 -eq 1 ]
then
	kolik="pivo"
elif [ $1 -gt 1 ] && [ 5 -gt $1 ]
then
	kolik="piva"
elif [ $1 -eq 0 ] || [ $1 -gt 4 ]
then
	kolik="piv"	
fi

echo "Das si $1 $kolik"

