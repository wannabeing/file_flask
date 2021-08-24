from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    from views import main_views, file_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(file_views.bp)

    # 에러 404 HTML 렌더링
    @app.errorhandler(404)
    def page_not_found(error):
         app.logger.error(error)  # 어떠한 오류나 특정 요청에 대한 로그를 남기고자 로깅을 한다. cmd 창에서 확인 가능
         return render_template('404.html'), 404

    return app
