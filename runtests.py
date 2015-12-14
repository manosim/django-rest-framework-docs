#!/usr/bin/env python
import sys
import subprocess


FLAKE8_ARGS = ['rest_framework_docs', '--ignore=E501']


def exit_on_failure(command, message=None):
    if command:
        sys.exit(command)


def flake8_main(args):
    print('Running: flake8', FLAKE8_ARGS)
    command = subprocess.call(['flake8'] + args)
    print("" if command else "Success. flake8 passed.")
    return command

exit_on_failure(flake8_main(FLAKE8_ARGS))
