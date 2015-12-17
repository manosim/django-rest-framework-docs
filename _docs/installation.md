---
title:  "Installation"
order: 2
---

The installation itself should not take more than a couple of minutes. Follow the simple steps below.

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
