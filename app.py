from flask import Flask, request, render_template
import os

app = Flask(__name__)

app.config['UPLOAD_FILE'] = "C:\\Users\\najwa\\Desktop\\"


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        que = request.files.getlist('file')
        for i in que:
            # i.save(file.filename)
            # request.files['file'].save(os.path.join(app.config['UPLOAD_FILE'], i.files['file'].filename))
            i.save(os.path.join(app.config['UPLOAD_FILE'], i.filename))
    return render_template('upload2.html')


if __name__ == '__main__':
    app.run(host='192.168.43.77', port=5000)