from flask import request
from ms.middlewares.middleware import Middleware, middleware


def test_middleware():
    class MockMiddleware(Middleware):
        def handler(self, request):
            return True

    @middleware(MockMiddleware)
    def mockFnc():
        return True

    assert Middleware.handler(Middleware, request) == None
    assert mockFnc() == True
    assert MockMiddleware().handler(request) == True
