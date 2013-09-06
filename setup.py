import os
from setuptools import setup, find_packages

#README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
README = """
Django REST Framework Docs

Rest Framework Docs is an application built to produce an inventory and documentation for your Django Rest Framework v2 endpoints.

Installation
From pip:

pip install django-rest-framework-docs

Docs & details @
https://github.com/marcgibbons/django-rest-framework-docs
"""

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-rest-framework-docs',
    version='0.1.7',
    download_url='https://github.com/marcgibbons/django-rest-framework-docs/raw/master/dist/django-rest-framework-docs-0.1.7.tar.gz',
    packages=['rest_framework_docs'],
    package_data={'rest_framework_docs': ['templates/rest_framework_docs/*']},
    include_package_data=True,
    license='FreeBSD License',
    description='An inventory tool for Django Rest Framework v2 API',
    long_description=README,
    install_requires=[
        'jsonpickle>=0.4.0',
        'django>=1.4',
        'djangorestframework>=2.1.3'
    ],

    url='http://github.com/marcgibbons',
    author='Marc Gibbons',
    author_email='marc_gibbons@rogers.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

