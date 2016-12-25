#!/bin/bash


echo -n "enter the pattern here: "
read pattern
initial=`echo $pattern|cut -c1`
export initial
export pattern
count=`./week1_1.py`

echo $count
