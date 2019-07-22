import socket
from flask import Flask, request, redirect, jsonify
from lib.shorter import Shorter
import urllib

app = Flask(__name__)

WEB_SERVER_IP = socket.gethostbyname(socket.gethostname())

@app.route('/url', methods=['POST'])
def shorter():
    url = request.form.get('ori_url', None)
    tinyurl = ''
    if url:
        urlencode = urllib.quote(url.split('://')[1])
        result, tinyurl = Shorter().validate(urlencode)
        if not result:
            tinyurl = Shorter().encode(urlencode, url)
        return jsonify({'code': 200, 'status': 200, 'message': tinyurl})
    else:
        return jsonify({'code': 200, 'status': 403, 'message': 'incorrect url'})     


@app.route("/<url_key>")
def redirect2ori(url_key):
    url = Shorter().decode(url_key)
    return redirect(url)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
