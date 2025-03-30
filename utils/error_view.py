from django.http import JsonResponse

def handle_404(request, exception):
    message = ('page not found')
    response = JsonResponse(data={'error':message})
    response.status_code = 404
    return response

def handle_500(request):
    message = ('Internal server error.')
    respone = JsonResponse(data={'error':message})
    respone.status_code = 500
    return respone

