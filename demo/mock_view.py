from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
    renderer_classes,
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.renderers import JSONRenderer

from django.conf.urls import url


class AnyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return


class JSONPRenderer(JSONRenderer):
    """
    jsonp render
    """

    media_type = "application/javascript"

    def render(self, data, accepted_media_type=None, renderer_context=None):

        renderer_context = renderer_context or {}
        request = renderer_context.get("request", None)
        callback = request.query_params.get("callback", "callback")

        json = super(JSONPRenderer, self).render(
            data, accepted_media_type, renderer_context
        )
        return callback.encode("utf-8") + b"(" + json + b");"


@api_view(["GET"])
@authentication_classes((AnyAuthentication,))
@permission_classes((AllowAny,))
@renderer_classes(
    (JSONPRenderer,),
)
def jsonp(request):
    token = request.COOKIES.get("auth", "")
    cookies = {
        "token": token,
        "host": request.get_host(),
    }

    response = Response(cookies)
    return response


@api_view(["POST"])
@authentication_classes((AnyAuthentication,))
@permission_classes((AllowAny,))
def login(request):
    token = request.COOKIES.get("auth", "auth")
    password = request.data.get("password", "")
    username = request.data.get("username", "")

    # user center check username password
    response = Response({"user": "user_info", "token": token})
    response.set_cookie("auth", token, domain="0.0.0.0", expires=30 * 24 * 60 * 60)
    return response


@api_view(["GET"])
@authentication_classes((AnyAuthentication,))
@permission_classes((AllowAny,))
def check_token(request, token):

    token = request.COOKIES.get("auth")

    # user center check token  ...

    data = {"user_info": {"username": "admin", "user_id": 1}, "token": token}
    return Response(data)


mock_urls = [
    url("^jsonp/", jsonp),
    url("^login/", login),
    url(r"^check_token/(?P<token>[A-Za-z0-9]+)/$", check_token),
]
