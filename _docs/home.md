---
title:  "Home"
permalink: /
order: 1
---

Django Rest Framework Docs (DRF Docs) allows you to list all your API Endpoints that inherit from <a href="http://www.django-rest-framework.org/" target="_blank">Django Rest Framework</a> **automatically**. Its purpose is to work out of the box and it should take a minimum to install it.

<a class="btn btn-success btn-demo" href="http://demo.drfdocs.com/" target="_blank"><i class="fa fa-laptop"></i> Check the Demo</a>

<h4>How It Works</h4>

<img class="img-responsive" src="static/images/mockup.png" alt="Mock Up" />

The concept is pretty simple. Once you [install it](/docs/installation/) you should go the the url you set (ie. `http://0.0.0.0:/8000/docs/`) and you should see all your API endpoints along with the serializer fields, allowed methods etc for each one.

DRF Docs will then read all your `urls` and will list those that inherit from Django Rest Framework's `APIView`.
