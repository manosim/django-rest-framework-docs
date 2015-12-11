# drf-docs [![Build Status](https://travis-ci.com/ekonstantinidis/drf-docs.svg?token=9QR4ewbqbkEmHps6q5sq&branch=master)](https://travis-ci.com/ekonstantinidis/drf-docs)
Documentation for Web APIs made with Django Rest Framework.


### Prerequisites

  - Python (3.3, 3.4, 3.5)
  - Django (1.8, 1.9)


### Development

    pyvenv env
    env/bin/pip install -r requirements.txt

### Installation

Install using pip...

    pip install drfdocs

Add 'rest_framework' to your INSTALLED_APPS setting.

    INSTALLED_APPS = (
        ...
        'drfdocs',
    )
