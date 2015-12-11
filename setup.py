from distutils.core import setup

setup(
    name="drf-docs",
    version="0.0.1",
    author="Emmanouil Konstantinidis",
    author_email="manos@iamemmanouil.com",
    packages=["drfdocs"],
    include_package_data=True,
    url="http://www.drfdocs.com",
    license='BSD',
    description="Documentation for Web APIs made with Django Rest Framework.",
    long_description=open("README.txt").read(),
    install_requires=[],
)
