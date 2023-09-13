from django.shortcuts import HttpResponse

class MyProcessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        return response


    def process_view(request, *args, **kwargs):
        print("This is process view Before view.")
        # return HttpResponse("This Is BeFore view")
        return None
        

class MyExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        return response


    def process_exception( self, request, exception):
        class_name = exception.__class__.__name__
        print(class_name)
        msg = exception
        print(msg)
        return HttpResponse(msg)
      
        

class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)
        return response


    def process_template_response(self, request, response):
        print("Process Template response from Middleware.")
        response.context_data['name'] = 'Hemi'
        return response
      
        