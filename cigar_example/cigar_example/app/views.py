# Create your views here.
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render_to_response
from django.template import RequestContext
from cigar_example.restapi import urls
from rest_framework_docs.docs import DocumentationGenerator
from django.http import HttpResponse


class ApiDocumentation(APIView):
    """
    Gets the documentation for the API endpoints
    """
    def get(self, *args, **kwargs):
        docs = DocumentationGenerator(urls.urlpatterns).get_docs()
        return Response(json.loads(docs))


def home(request):
    return render_to_response('index.html')



