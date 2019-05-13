#!/bin/bash

echo "------------------------------------------------------------------------------------"

echo "Select a game"
echo "1. Guess our Number"
echo "2. Thinker: We (try to) guess your number"

valid=true
var=""
while [ $valid ]
do
    echo -n "> (e to exit) "
    read var
    if [ $var -eq 1 ]
    then
        python3.6 "$PWD/bin/four_number_game/four_number_game.py"
    fi

    if [ $var -eq 2 ]
    then
        python3.6 ./bin/thinker/thinker
    fi

    if [ $var -eq e ]
    then
        $valid=false
    fi


done