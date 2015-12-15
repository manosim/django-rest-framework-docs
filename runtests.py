#!/usr/bin/env python
import os
import sys
import subprocess
import django
from django.conf import settings
from django.test.utils import get_runner


FLAKE8_ARGS = ['demo/project/', 'rest_framework_docs', 'tests/', '--ignore=E501']


def exit_on_failure(command, message=None):
    if command:
        sys.exit(command)


def flake8_main(args):
    print('Running: flake8', FLAKE8_ARGS)
    command = subprocess.call(['flake8'] + args)
    print("" if command else "Success. flake8 passed.")
    return command


def django_tests_main():
    if __name__ == "__main__":
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
        django.setup()
        TestRunner = get_runner(settings)
        test_runner = TestRunner()
        failures = test_runner.run_tests(["tests"])
        sys.exit(bool(failures))

exit_on_failure(flake8_main(FLAKE8_ARGS))

django_tests_main()
