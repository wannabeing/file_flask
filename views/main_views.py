from flask import Blueprint, url_for
from werkzeug.utils import redirect
from blog import *

bp = Blueprint('main', __name__, url_prefix='/')


# 메인페이지 HTML 렌더링
@bp.route('/')
def home_page():
    return render_template('login.html')


