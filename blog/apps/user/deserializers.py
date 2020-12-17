from blog.common.base_schema import BaseSchema
from marshmallow import fields


class UserObjSerializers(BaseSchema):
    """
    根据用户id 获取用户相关信息
    """
    u_id = fields.Integer(doc='用户id')
    name = fields.String(doc='用户相关信息')
