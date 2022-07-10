from rest_framework import exceptions, status
from rest_framework.views import APIView


class MyApiView(APIView):
    def handle_exception(self, exc):
        if isinstance(exc, (exceptions.NotAuthenticated,
                            exceptions.AuthenticationFailed)):
            auth_header = self.get_authenticate_header(self.request)
            print(auth_header)
            if auth_header:
                exc.auth_header = auth_header
            else:
                exc.status_code = status.HTTP_403_FORBIDDEN

        exception_handler = self.get_exception_handler()

        context = self.get_exception_handler_context()
        response = exception_handler(exc, context)

        if response is None:
            self.raise_uncaught_exception(exc)

        response.exception = True
        response.status_code = 200
        return response
