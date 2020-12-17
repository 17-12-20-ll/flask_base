import json
import re
import logging
import time
import traceback
from functools import wraps

from flask import request
from flask_restful import Resource
from flask_restful import ResponseBase
from flask import make_response

from blog.config import Config

logger = logging.getLogger(__name__)


def xml(data, code, headers):
    if not isinstance(data, str):
        data = str(data)
    resp = make_response(data, code)
    headers and resp.headers.extend(headers)
    return resp


def json_out(data, code, headers):
    resp = make_response(json.dumps(data), code)
    headers and resp.headers.extend(headers)
    return resp


Resource.representations = {
    'application/json': json_out,
    'application/xml': xml,
}


def except_middleware(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = None
        try:
            logger.info(
                '[%s]: request url %s',
                re.sub(r"\s.*", "", re.sub(r'.*method\s', "", func.__str__().replace("<function ", ""))),
                request.url
            )
            logger.info('request params %s', request.data or request.form.to_dict())
            logger.info('request headers %s', request.headers)
            logger.info('request cookies %s', request.cookies)
            result = func(*args, **kwargs)
        except Exception as E:
            logger.error(traceback.format_exc())
            result = [{"error_code": 500, "error_msg": "服务错误，请重试！"}, 500, None]
        finally:
            from werkzeug import Response
            if isinstance(result, (ResponseBase, Response)):
                return result
            result = list(result)
            if isinstance(result[0], str) and result[1] != 200:
                result[0] = {'error_code': 400, 'error_msg': result[0]}
            end_time = time.time()
            logger.info(
                '[%s]: request response %s %s',
                re.sub(r"\s.*", "", re.sub(r'.*method\s', "", func.__str__())),
                result,
                end_time - start_time
            )
            return tuple(result)

    return wrapper


def authorization_middleware(func):
    """用户登录凭证认证"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        login_credential = request.headers.get('Login-Credential')
        result = func(*args, **kwargs)
        return result

    return wrapper


class BaseView(Resource):
    method_decorators = [except_middleware]


class AuthBaseView(BaseView):
    method_decorators = [authorization_middleware, except_middleware]
