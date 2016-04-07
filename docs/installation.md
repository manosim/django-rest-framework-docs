---
source_filename: installation
---

The installation itself should not take more than a couple of minutes. Follow the simple steps below.

### Install from PyPI

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

You can now visit [http://0.0.0.0:/8000/docs/](http://0.0.0.0:8000/docs/) to view your Web API's docs.
