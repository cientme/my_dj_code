

def my_middleware(get_response):
    print('One Time Initialization')
    def my_function(request):
        print('This is Before view')
        response = get_response(request)
        print('This is fter view')
        return response
    return my_function
