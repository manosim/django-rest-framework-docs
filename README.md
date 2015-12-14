# [Django Rest Framework Docs](http://www.drfdocs.com/) [![travis][travis-image]][travis-url] [![pypi][pypi-image]][pypi-url]

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

    pip install djangorestframeworkdocs

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

### Development & Demo Project
Included in this repo you can find the demo project(at `/demo`). It is a project with *Django* & *Django Rest Framework* that will allow you to work with this project. For more information on how you can set it up please readme the [README.md](demo/README.md) of the demo project.

### Settings

    REST_FRAMEWORK_DOCS = {
        'HIDDEN': True  # Default: False
    }

### Roadmap

  - [ ] Support Python 2 & Python 3
  - [ ] Support DRF 3+
  - [ ] Open Pull Request to include in DRF
  - [ ] Submit to djangopackages.com


### Credits

First of all thanks to the [Django](http://www.djangoproject.com/) core team and to all the contributors of [Django REST Framework](http://www.django-rest-framework.org/) for their amazing work. Also I would like to thank [Marc Gibbons](https://github.com/marcgibbons) for his *django-rest-framework-docs* project. Both projects share the same idea, it is just that Marc's is not maintained anymore and does not support DRF 3+ & Python 3.

[travis-image]: https://travis-ci.com/ekonstantinidis/django-rest-framework-docs.svg?token=9QR4ewbqbkEmHps6q5sq&branch=master
[travis-url]: https://travis-ci.com/ekonstantinidis/django-rest-framework-docs

[pypi-image]: https://img.shields.io/pypi/v/djangorestframeworkdocs.svg
[pypi-url]: https://pypi.python.org/pypi/djangorestframeworkdocs/
