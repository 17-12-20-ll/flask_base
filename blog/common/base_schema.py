from marshmallow import Schema


class BaseSchema(Schema):
    class Meta:
        strict = True  # 通过抛异常的方式提示错误
        unknown = True
