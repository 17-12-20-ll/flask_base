import os
import sys

# 初始化环境
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from blog import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7019, debug=True)
else:
    application = app
