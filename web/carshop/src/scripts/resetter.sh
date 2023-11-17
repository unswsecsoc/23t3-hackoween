#!/bin/sh

cd /

reset_script=$(ls | grep secret_reset_script)
socat TCP4-LISTEN:1337,fork EXEC:"sh ./$reset_script"
