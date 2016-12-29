import flask
import os
from flask import Flask
from flask import Flask
from flask import request
from leecher import search4zimu

application = flask.Flask(__name__)

# Only enable Flask debugging if an env var is set to true
application.debug = os.environ.get('FLASK_DEBUG') in ['true', 'True']

# Get application version from env
app_version = os.environ.get('APP_VERSION')

# Get cool new feature flag from env
enable_cool_new_feature = os.environ.get('ENABLE_COOL_NEW_FEATURE') in ['true', 'True']

@application.route('/')
def hello_world():
    message = "Hello, world!"
    return flask.render_template('index.html',
                                  title=message,
                                  flask_debug=application.debug,
                                  app_version=app_version,
                                  enable_cool_new_feature=enable_cool_new_feature)
@application.route('/search')
def search():
    keyword = request.args.get('keyword', '')
    result = search4zimu(keyword.encode('utf-8'))
    urls = []
    names = []
    for k,v in result.items():
        print k,v
        urls.append(k)
        names.append(v)
    return urls[0]


if __name__ == '__main__':
    application.run()
