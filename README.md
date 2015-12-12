# drf-docs [![Build Status](https://travis-ci.com/ekonstantinidis/drf-docs.svg?token=9QR4ewbqbkEmHps6q5sq&branch=master)](https://travis-ci.com/ekonstantinidis/drf-docs)
Documentation for Web APIs made with Django Rest Framework.


### Prerequisites

  - Python (3.3, 3.4, 3.5)
  - Django (1.8, 1.9)
  - Django Rest Framework (3+)


### Development

    pyvenv env
    env/bin/pip install -r requirements.txt

    # To test within another django project
    pip install -e ~/Projects/drf-docs/

### Installation

Install using pip:

    pip install drfdocs

Add 'drfdocs' to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        'drfdocs',
    )

Finally include the `drfdocs` urls in your `urls.py`:

    urlpatterns = [
        ...
        url(r'^docs/', include('drfdocs.urls', app_name='drfdocs', namespace='drfdocs')),
    ]
