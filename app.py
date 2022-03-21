import os

from flask import Flask, request, render_template, make_response, redirect, url_for


app = Flask(__name__,
            static_url_path='',
            static_folder='web/public/static',
            template_folder='web/public/templates')


@app.route('/', methods=['GET'])
def greet():
    return 'Welcome to IATA One Record Workshop :-)', 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))