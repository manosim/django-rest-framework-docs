---
title:  "Changelog"
source_filename: "changelog"
---

### Release 0.0.10

  - Use get_serializer_class for Views without serlaizer_class attribute [#92](https://github.com/ekonstantinidis/django-rest-framework-docs/pull/92)


### Release 0.0.9

  - Support for more types of `ROOT_URLCONF`
  - Move docs to [MKDocs](http://www.mkdocs.org/)


### Release 0.0.7

  - Fix methods in Live API Endpoints (now compatible with Python 2.7)
  - Remove `.<format>` from urls
  - Fixed a bug that removes double slashes from the endpoint's url


### Release 0.0.6

  - Introducing Live API Endpoints - Test your endpoints from within the docs
  - Setting `HIDDEN` is now `HIDE_DOCS`


### Release 0.0.5

  - Support both common types of `ROOT_URLCONF`


### Release 0.0.4

  - Allow templates overrides
  - More template `blocks` to be overridden
  - Improved MANIFEST.in
  - Exclude `node_modules/`


### Release 0.0.3

  - Fixes a bug where Django's `collectstatic` command was failing because of Glyphicons


### Release 0.0.2

  - Search between endpoint paths
  - Display docstring for each endpoint


### Release 0.0.1

First release of the project to [pypi](https://pypi.python.org/pypi). Features include:

 - List all endpoints that inherit from DRF's `APIView`
 - Settings to hide docs view (ie. in Production)
 - Override Templates
 - Support for Python 2.7, 3.3, 3.4, 3.5
 - Support for Django 1.8, 1.9
 - Support for Django REST Framework 3 and above
