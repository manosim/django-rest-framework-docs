# drf-docs [![travis][travis-image]][travis-url] [![pypi][pypi-image]][pypi-url]

Document Web APIs made with Django Rest Framework.


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

[travis-image]: https://travis-ci.com/ekonstantinidis/drf-docs.svg?token=9QR4ewbqbkEmHps6q5sq&branch=master
[travis-url]: https://travis-ci.com/ekonstantinidis/drf-docs

[pypi-image]: https://img.shields.io/pypi/v/drfdocs.svg
[pypi-url]: https://pypi.python.org/pypi/drffocs/
