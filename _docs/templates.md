---
title:  "Extending the Template"
source_filename: "templates"
order: 4
---

### Create the template file
To edit the template you will have to create a `.html` file to override the original one. Inside your `templates` directory create a directory named `rest_framework_docs` and inside this create the file `docs.html`. You can then extend/override the default template.

    {% raw %}
    {% extends "rest_framework_docs/base.html" %}
    {% endraw %}


### Default Blocks


#### Styles (CSS)

    {% raw %}
    {% block style %}
    <link rel="stylesheet" href="{% static "path/to/custom/css/style.css" %}">
    {% endblock %}
    {% endraw %}

#### GitHub Badge
To hide the GitHub badge from the page, just override it with an empty block.

    {% raw %}{% block github_badge %}{% endblock %}{% endraw %}

#### Title

    {% raw %}{% block title %}Project Name{% endblock %}{% endraw %}

#### Logo

    {% raw %}
    {% block logo %}
      <a class="navbar-brand" href="http://www.drfdocs.com/">DRF Docs</a>
    {% endblock %}
    {% endraw %}

#### Jumbotron

    {% raw %}
    {% block jumbotron %}
    <div class="jumbotron">
      <h1>Project Title</h1>
      <h3>Documentantion of the project 'Example'.</h3>
    </div>
    {% endblock %}
    {% endraw %}

#### Footer

    {% raw %}
    {% block footer %}
      <div class="footer">
        <div class="links">
          <a href="http://www.iamemmanouil.com"><i class="fa fa-link"></i></a>
          <a href="http://www.github.com/ekonstantinidis"><i class="fa fa-github"></i></a>
          <a href="http://www.twitter.com/iamemmanouil"><i class="fa fa-twitter"></i></a>
        </div>
        Copyright © 2015 Emmanouil Konstantinidis.
      </div>
    {% endblock %}
    {% endraw %}


### Complete Example
File location: `templates/rest_framework_docs/docs.html`

    {% raw %}
    {% extends "rest_framework_docs/base.html" %}

    {% block title %}Project Name{% endblock %}
    {% block logo %}<a class="navbar-brand" href="#"">Project Name API Documentation</a>{% endblock %}

    {% block jumbotron %}
    <div class="jumbotron">
      <h1>'Project Name' Web API</h1>
      <h3>Documentantion of the 'Project Name' Web API.</h3>
    </div>
    {% endblock %}

    {% block footer %}<div class="footer">Copyright © 2015 Project Name.</div>{% endblock %}

    {% endraw %}
