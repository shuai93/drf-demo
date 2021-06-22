from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response


class CustomException(Exception):
    # 自定义code
    default_code = 400
    # 自定义 message
    default_message = None

    def __init__(
            self,
            status_code=status.HTTP_400_BAD_REQUEST,
            code: int = None,
            message: str = None,
            data=None,
    ):
        self.status = status_code
        self.code = self.default_code if code is None else code
        self.message = self.default_message if message is None else message

        if data is None:
            self.data = {"detail": self.message, "code": self.code}
        else:
            self.data = data

    def __str__(self):
        return str(self.code) + self.message


class ExecuteError(CustomException):
    """执行出错"""
    default_code = 500
    default_message = "执行出错"


class UnknownError(CustomException):
    """执行出错"""
    default_code = 500
    default_message = "未知出错"


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.

    if isinstance(exc, CustomException):
        return Response(data=exc.data, status=exc.status)
    response = exception_handler(exc, context)
    return response
