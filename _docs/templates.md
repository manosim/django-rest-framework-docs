---
title:  "Extending the Template"
source_filename: "templates"
order: 4
---

### Create the template file
To edit the template you will have to create a `.html` file to override the original one. Inside your `templates` directory create a directory named `rest_framework_docs` and inside this create the file `base.html`. You can then extend/override the default template.

    {% raw %}
    {% extends "rest_framework_docs/base.html" %}
    {% endraw %}


### Default Blocks

#### Logo

    {% raw %}
    {% block logo %}
      <a class="navbar-brand" href="http://www.drfdocs.com/">DRF Docs</a>
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


### Example

    {% raw %}
    {% extends "rest_framework_docs/base.html" %}

    {% block footer %}
      <div class="footer">
        Copyright © 2015 Project Name.
      </div>
    {% endblock %}

    {% endraw %}
