from flasgger_marshmallow import swagger_decorator
from flask import request

from .bll import user_get
from .deserializers import UserObjSerializers
from .serializers import UserGetDeserializers
from blog.common.res_auth import BaseView


class User(BaseView):
    @swagger_decorator(query_schema=UserGetDeserializers, response_schema={200: UserObjSerializers})
    def get(self):
        """
        获取用户相关信息
        用户相关信息
        """
        query_schema = request.query_schema
        return user_get(query_schema)

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
