import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-rest-framework-docs',
    version='0.1.0',
    packages=['rest_framework_docs'],
    package_data={'rest_framework_docs': ['templates/rest_framework_docs/*']},
    include_package_data=True,
    license='FreeBSD License',
    description='An inventory tool for Django Rest Framework v2 API endpoints.',
    long_description=README,
    install_requires=[
        'jsonpickle>=0.4.0',
        'django==1.4',
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

