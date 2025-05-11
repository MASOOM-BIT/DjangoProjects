from django.http import HttpResponse
class MiddleWareLifeCycle:
    def __init__(self,get_response):
        print("Middleware initialized")
        self.get_response = get_response

    def __call__(self, request):
        print("Before view is executed")
        response = self.get_response(request)
        print("After view is executed")
        return response
        
class ExceptionHandlingMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    
    def process_exception(self, request, exception):
        print("Exception occurred")
        return HttpResponse("An error occurred: " + str(exception))
