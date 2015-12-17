---
title:  "Extending the Template"
source_filename: "templates"
order: 4
---

### Create the template file



### Default Block


##### Logo

    { % block logo % }
      <a class="navbar-brand" href="http://www.drfdocs.com/">DRF Docs</a>
    { % endblock % }

##### Footer

    { % block footer % }
      <div class="footer">
        <div class="links">
          <a href="http://www.iamemmanouil.com"><i class="fa fa-link"></i></a>
          <a href="http://www.github.com/ekonstantinidis"><i class="fa fa-github"></i></a>
          <a href="http://www.twitter.com/iamemmanouil"><i class="fa fa-twitter"></i></a>
        </div>
        Copyright © 2015 Emmanouil Konstantinidis.
      </div>
    { % endblock % }
