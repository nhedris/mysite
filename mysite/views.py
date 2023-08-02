from django.http import HttpResponse,jsonResponse

def http_test(request):
    return HttpResponse ('<h1> heloooo<\h1>')

def json_test(request):
    return jsonResponse ({"hiii"})