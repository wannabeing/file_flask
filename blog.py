from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 파입 업로드 용량 제한


# 메인페이지 HTML 렌더링
@app.route('/')
def home_page():
    return render_template('index.html')


# 파일 리스트 HTML 렌더링
@app.route('/list')
def list_page():
    file_list = os.listdir("./uploads")
    # html = """ <center><a href="/">홈페이지</a><br><br>"""
    # html += "file_list: {}".format(file_list) + "</center>"
    # return html
    return render_template('list.html', file_list=file_list)


# 업로드 HTML 렌더링
@app.route('/upload')
def upload_page():
    return render_template('upload.html')


# 파일 업로드 처리
@app.route('/uploadcheck', methods =['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file'] # POST 방식으로 업로드페이지에서 넘어오면 file이라는 이름의 폼으로 전송된 파일을 가져옴
        file.save('./uploads/'+secure_filename(file.filename)) # 파일이름을 보호하고 file.save로 파일 객체를 지정한 폴더에 저장한다
        file_list = os.listdir("./uploads")
        return render_template('check.html', file_list=file_list)


# 다운로드 HTML 렌더링
@app.route('/download')
def down_page():
    file_list = os.listdir("./uploads")
    return render_template('download.html', file_list=file_list)


# 파일 다운로드 처리
@app.route('/fileDownload', methods = ['GET','POST'])
def down_file():
    if request.method == 'POST':
        sw = 0
        file_list = os.listdir("./uploads")
        for x in file_list:
            if(x==request.form['file']):
                sw = 1
        path = "./uploads/"
        return send_file(path + request.form['file'],
                         attachment_filename=request.form['file'],
                         as_attachment=True)


# 에러 404 HTML 렌더링
@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)  # 어떠한 오류나 특정 요청에 대한 로그를 남기고자 로깅을 한다. cmd 창에서 확인 가능
    return render_template('404.html'), 404


# 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)