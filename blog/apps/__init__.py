from blog.common import app
from blog.apps.user import user_bp

# 初始化路由
app.register_blueprint(user_bp, url_prefix='/api/user')
