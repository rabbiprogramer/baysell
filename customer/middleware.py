class LastSeenMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response


    def __call__(self,request):
        if request.user.is_authenticated:
            print('User is authenticated')
        else:
            print('User is notauthenticated')
        response = self.get_response(request)
        return  response

            



