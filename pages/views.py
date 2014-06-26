from django.views.decorators.http import require_http_methods
from django.shortcuts import render_to_response

@require_http_methods(["GET"])
def index(request):
  return render_to_response('pages/index.html')
