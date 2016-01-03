#!/usr/bin/env python
import os
import sys
import subprocess
import django
from coverage import coverage
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


def run_tests_eslint():
    print('Running: eslint')
    command = subprocess.call(['cd rest_framework_docs/static/ && npm test'], shell=True)
    print("" if command else "Success. eslint passed.")
    return command


def run_tests_coverage():
    if __name__ == "__main__":
        os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
        django.setup()
        TestRunner = get_runner(settings)
        test_runner = TestRunner()

        # Setup Coverage
        cov = coverage(source=["rest_framework_docs"], omit=["rest_framework_docs/__init__.py"])
        cov.start()

        failures = test_runner.run_tests(["tests"])

        if bool(failures):
            cov.erase()
            sys.exit("Tests Failed. Coverage Cancelled.")

        # If success show coverage results
        cov.stop()
        cov.save()
        cov.report()
        cov.html_report(directory='covhtml')

exit_on_failure(flake8_main(FLAKE8_ARGS))
exit_on_failure(run_tests_eslint())
exit_on_failure(run_tests_coverage())
