import pyscreenshot
import flask
from io import BytesIO

LOGO = "\n\t  _____  __   __ _______ _______  ______ _______ _______ _______\n\t |_____]   \_/   |______    |    |_____/ |______ |_____| |  |  |\n\t |          |    ______|    |    |    \_ |______ |     | |  |  |\n\t                                                                \n\t"

app = flask.Flask(__name__)

@app.route('/screen.png')
def serve_pil_image():
    img_buffer = BytesIO()
    pyscreenshot.grab().save(img_buffer, 'PNG', quality=100)
    img_buffer.seek(0)
    return flask.send_file(img_buffer, mimetype='image/png')


@app.route('/js/<path:path>')
def send_js(path):
    return flask.send_from_directory('js', path)


@app.route('/')
def serve_img():
    return flask.render_template('screen.html')


def main():
    app.run(host='0.0.0.0', debug=True, threaded=True)

if __name__ == '__main__':
    main()

