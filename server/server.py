from flask_cors import CORS
from flask import Flask
import subprocess


GIT_LOG_COMMAND = 'git log'

SSL_CERTIFICATE_PATH = '/etc/letsencrypt/live/npanuhin.me/fullchain.pem'
SSL_CERTIFICATE_KEY_PATH = '/etc/letsencrypt/live/npanuhin.me/privkey.pem'

app = Flask(__name__)
CORS(app)


def get_git_log_data():
    git_log_result = subprocess.run(GIT_LOG_COMMAND, shell=True, stdout=subprocess.PIPE, text=True)  # noqa
    return git_log_result.stdout.encode()


@app.route('/')
def git_log():
    return get_git_log_data()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2096, ssl_context=(SSL_CERTIFICATE_PATH, SSL_CERTIFICATE_KEY_PATH))
