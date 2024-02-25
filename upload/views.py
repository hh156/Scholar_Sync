from django.http import HttpResponse
from django.shortcuts import loader


# Create your views here.
def upload(request):
    template = loader.get_template('uploadPage.html')
    return HttpResponse(template.render())