from django.http import HttpResponse

def commodityView(request):
    return HttpResponse('Hello World')

def detailView(request, id):
    return HttpResponse('Hello World')