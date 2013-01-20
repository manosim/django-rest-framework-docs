===========================
Rest Framework Docs (0.1.0)
===========================

Rest Framework Docs is an application built to produce an inventory
and documentation for you Django Rest Framework v2 endpoints.

Quick start
-----------

1. Add "rest_framework_docs" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'rest_framework_docs',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^rest-api/', include('rest_framework_docs.urls')),


3. View /rest-api/docs to see you Django Rest Framework endpoints


How it works
------------

The Django Rest Framework Docs scans your projects URL patterns for endpoints
inheriting from Django Rest Framework views. Here are the components used to
generate documentation for your endpoints:

1)  The name attribute from the URL pattern is used as the title
    url(r'^api/countries/?$', views.Countries.as_view(), name='list_of_countries'),

2)  The class doctsring is used as the description::

		class Countries(APIView):
		    """
		    This text is the description for this API
		    """

3)  The class model. (ie. User)

4)  Allowed methods (GET, POST, PUT, etc.)

5)  Serializer properties. If your API uses a serializer, the properties are
    listed

5)  Custom parameters. It is possible to customize a parameter list for your
    API. To do so, include a key-value pair in the docstring of your API class
    delimited by two hyphens ('--').

    Example: 'start_time -- The first reading'::

	    class Countries(APIView):
	        """
	        This text is the description for this API
		param1 -- A first parameter
		param2 -- A second parameter
	        """

Many thanks to Tom Christie for developing the Django Rest Framework.
