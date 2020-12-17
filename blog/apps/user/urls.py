from blog.common.utils import AddResources

from .views import User

ar = AddResources('user')

r_s = [
    (User, '/v1'),
]

user_bp = ar.to_api(resources_apis=r_s)
