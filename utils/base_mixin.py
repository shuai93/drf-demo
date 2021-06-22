
import logging

from rest_framework.decorators import action


from utils.custom_exception import CustomException, UnknownError, ExecuteError

logger = logging.getLogger('demo')


class ExceptionMixin(object):

    @action(detail=False, methods=["get"], url_name="exception", url_path="exception")
    def custom_exception(self, request, *args, **kwargs):
        # 日志使用 demo
        logger.error("自定义异常")
        raise CustomException(data={"detail": "自定义异常"})

    @action(detail=False, methods=["get"], url_name="unknown", url_path="unknown")
    def unknown_error(self, request, *args, **kwargs):
        # 日志使用 demo
        logger.error("未知错误")
        raise UnknownError()

    @action(detail=False, methods=["get"], url_name="execute", url_path="execute")
    def execute_error(self, request, *args, **kwargs):
        # 日志使用 demo
        logger.error("执行错误")
        raise ExecuteError()
