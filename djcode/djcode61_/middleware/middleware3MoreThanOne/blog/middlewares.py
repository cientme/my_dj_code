from django.http import HttpResponse

class BrotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('One Time Brother Initialization')
        
    def __call__(self, request):
        print('This Is Brother Before View')
        response = self.get_response(request)
        print('This Is Brother After View')  
        return response     

class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    print('One Time Father Initialization')

    def __call__(self, request):
        print("This is Father Before View")
        response = self.get_response(request)
        # response = HttpResponse("Nikl Lo Pelei Fursat m")
        print("This Is Father After View")
        return response


class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Mother Initilization")

    def __call__(self, request):
        print("This Is Mother Before View")
        response = self.get_response(request)
        print("This Is Mother After View")
        return response
