from blog.common.base_schema import BaseSchema
from marshmallow import fields


class UserGetDeserializers(BaseSchema):
    u_id = fields.String(doc='用户id', required=True)
