from setuptools import find_packages, setup

setup(
    name="drf-docs",
    version=__import__('drfdocs').__version__,
    author="Emmanouil Konstantinidis",
    author_email="manos@iamemmanouil.com",
    packages=find_packages(),
    include_package_data=True,
    url="http://www.drfdocs.com",
    license='BSD',
    description="Documentation for Web APIs made with Django Rest Framework.",
    long_description=open("README.txt").read(),
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
