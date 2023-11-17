#!/bin/sh

mv /app/flag.txt /app/flag_`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 5 | head -n 1`
mv /secret_reset_script.sh /secret_reset_script_`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 5 | head -n 1`.sh

