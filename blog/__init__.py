import logging.config
from flasgger import Swagger

from blog.apps import app
from blog.common import db
from blog.common.log import config_logger

# 日志初始化

logging.config.dictConfig(config_logger())
logger = logging.getLogger(__name__)
# swagger 配置
Swagger(
    app,
    config={
        "debug": True,
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/api/blog/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/api/blog/flasgger_static",
        # "static_folder": "static",  # must be set by user
        "swagger_ui": True,
        "specs_route": "/api/blog/apidocs/"
    }
)

db.init_app(app)
