# [Django Rest Framework Docs](http://www.drfdocs.com/) [![travis][travis-image]][travis-url] [![pypi][pypi-image]][pypi-url]

Document Web APIs made with Django Rest Framework.


### Supports

  - Python (2.7, 3.3, 3.4, 3.5)
  - Django (1.8, 1.9)
  - Django Rest Framework (3+)


### Development & Demo Project
If you are looking to develop this package with one of your own django projects:

    pyvenv env
    env/bin/pip install -r requirements.txt
    pip install -e ~/Projects/drf-docs/

If you want to use the demo app to work on this package:
Included in this repo you can find the demo project(at `/demo`). It is a project with *Django* & *Django Rest Framework* that will allow you to work with this project. For more information on how you can set it up please check the [README.md](demo/README.md) of the demo project.

### Installation

Install using pip:

    pip install drfdocs

Add 'rest_framework_docs' to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        'rest_framework_docs',
    )

Finally include the `rest_framework_docs` urls in your `urls.py`:

    urlpatterns = [
        ...
        url(r'^docs/', include('rest_framework_docs.urls')),
    ]


### Settings

    REST_FRAMEWORK_DOCS = {
        'HIDDEN': True  # Default: False
    }


### Credits

First of all thanks to the [Django](http://www.djangoproject.com/) core team and to all the contributors of [Django REST Framework](http://www.django-rest-framework.org/) for their amazing work. Also I would like to thank [Marc Gibbons](https://github.com/marcgibbons) for his *django-rest-framework-docs* project. Both projects share the same idea, it is just that Marc's is not maintained anymore and does not support DRF 3+ & Python 3.

[travis-image]: https://travis-ci.org/ekonstantinidis/django-rest-framework-docs.svg?branch=master
[travis-url]: https://travis-ci.org/ekonstantinidis/django-rest-framework-docs

[pypi-image]: https://img.shields.io/pypi/v/drfdocs.svg
[pypi-url]: https://pypi.python.org/pypi/drfdocs/
