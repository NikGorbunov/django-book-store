from books.models import SaveHttpRequests


def save_requests_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request_path = request.build_absolute_uri()
        request_method = request.method
        request_instance = SaveHttpRequests(request_method=request_method, request_path=request_path)
        request_instance.save()

        response = get_response(request)

        return response

    return middleware
