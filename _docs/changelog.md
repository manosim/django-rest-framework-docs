---
title:  "Changelog"
source_filename: "changelog"
order: 5
---

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
 - Support for Django Rest Framework 3 and above
