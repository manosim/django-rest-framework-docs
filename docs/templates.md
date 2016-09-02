---
source_filename: templates
---

### Create the template file
To edit the template you will have to create a `.html` file to override the original one. Inside your `templates` directory create a directory named `rest_framework_docs` and inside this create the file `docs.html`. You can then extend/override the default template.

    {% extends "rest_framework_docs/base.html" %}


### Default Blocks

##### Styles (CSS)

    {% block style %}
    <link rel="stylesheet" href="{% static "path/to/custom/css/style.css" %}">
    {% endblock %}

##### GitHub Badge
To hide the GitHub badge from the page, just override it with an empty block.

    {% block github_badge %}{% endblock %}

##### Title

    {% block title %}Project Name{% endblock %}

##### Logo

    {% block logo %}
      <a class="navbar-brand" href="http://www.drfdocs.com/">DRF Docs</a>
    {% endblock %}

##### Jumbotron

    {% block jumbotron %}
    <div class="jumbotron">
      <h1>Project Title</h1>
      <h3>Documentation of the project 'Example'.</h3>
    </div>
    {% endblock %}

##### Footer

    {% block footer %}
      <div class="footer">
        <div class="links">
          <a href="http://www.manosim.com"><i class="fa fa-link"></i></a>
          <a href="http://www.github.com/manosim"><i class="fa fa-github"></i></a>
          <a href="http://www.twitter.com/iamemmanouil"><i class="fa fa-twitter"></i></a>
        </div>
        Copyright © 2016 Emmanouil Konstantinidis.
      </div>
    {% endblock %}


### Complete Example
File location: `templates/rest_framework_docs/docs.html`

    {% extends "rest_framework_docs/base.html" %}

    {% block title %}Project Name{% endblock %}
    {% block logo %}<a class="navbar-brand" href="#"">Project Name API Documentation</a>{% endblock %}

    {% block jumbotron %}
    <div class="jumbotron">
      <h1>'Project Name' Web API</h1>
      <h3>Documentation of the 'Project Name' Web API.</h3>
    </div>
    {% endblock %}

    {% block footer %}<div class="footer">Copyright © 2016 Project Name.</div>{% endblock %}
