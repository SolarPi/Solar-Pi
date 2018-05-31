#!/bin/bash
RANGE=2

number=$RANDOM
let "number %= $RANGE"
case $number in
    0)
        cow="default"
        ;;
    1)
        cow="tux"
        ;;
esac

RANGE=2
number=$RANDOM
let "number %= $RANGE"
case $number in
    0)
        command="cowsay"
        ;;
    1)
        command="cowthink"
        ;;
esac
fortune | $command -f $cow | lolcat
echo