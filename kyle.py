from flask import Flask, render_template
app = Flask(__name__)

app.debug = True

from local_config import FACEBOOK_APP_ID

@app.route('/')
def home():

    return render_template('home.html', fb_app_id=FACEBOOK_APP_ID)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
