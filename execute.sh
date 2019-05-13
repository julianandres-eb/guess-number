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
        /home/jagadru/PycharmProjects/eventbrite/venv/bin/python /home/jagadru/PycharmProjects/eventbrite/bin/four_number_game/four_number_game.py
    fi

    if [ $var -eq 2 ]
    then
        /home/jagadru/PycharmProjects/eventbrite/venv/bin/python /home/jagadru/PycharmProjects/eventbrite/bin/thinker/thinker.py
    fi

    if [ $var -eq e ]
    then
        $valid=false
    fi
done