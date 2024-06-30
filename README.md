python3 -m venv filestation

source file-transfer-env/bin/activate
or
FileStation\Scripts\activate

pip install flask flask-uploads



如果遇到
from werkzeug import secure_filename, FileStorage
ImportError: cannot import name 'secure_filename' from 'werkzeug'
这样的报错，是Flask-Uploads包当前版本（0.2.1）的一个bug，需进入环境代码中修改flask_uploads.py，将
from werkzeug import secure_filename, FileStorage
修改为
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
