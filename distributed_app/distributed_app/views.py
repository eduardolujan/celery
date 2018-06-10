from django.http import HttpResponse

def test_sum(request):
    return HttpResponse('OK')