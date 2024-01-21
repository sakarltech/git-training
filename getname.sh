#!/bin/bash
echo "ENTER YOUR NAME"
read name
echo "The name given was: $name". Could you kindly confirm?
read reply
if [ "$reply" == yes ]; then
	echo "Perfect! Thanks for confirming"
else
	echo "my bad! I must have missed it."
	echo "Please ENTER YOUR NAME AGAIN"
read name
echo "The name entered is: $name and I am sure I got it this time"
echo "No need to re-enter name"
fi 
