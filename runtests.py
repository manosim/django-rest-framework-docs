#!/usr/bin/env python
import os
import sys
import subprocess


FLAKE8_ARGS = ['drfdocs', '--ignore=E501']

def exit_on_failure(command, message=None):
    if command:
        sys.exit(command)

def flake8_main(args):
    print('Running: flake8', *FLAKE8_ARGS, sep=' ')
    command = subprocess.call(['flake8'] + args)
    print("" if command else "Success. flake8 passed.")
    return command

exit_on_failure(flake8_main(FLAKE8_ARGS))
