#!/bin/bash

if [[ $# -ne 1 ]]
then
	echo "Error: invalid amount parameter"
	exit 1
fi

if [ $1 ]
then
	curl -s $1 | grep "moved here" | cut -d '"' -f 2
else
	echo "Error: no parameter"
	exit 1
fi

