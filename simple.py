import subprocess

## Do some processing in Python

## Set do-file information
dofile = "/Users/andrewlocke/Documents/Git/testStataRepository/simple.do"
cmd = ["stata", "do", dofile, "mpg", "weight", "foreign"]

## Run do-file
subprocess.call(cmd) 