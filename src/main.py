# encoding: utf-8

from bottle import default_app, run
from route.route import *
from static.static import *
from jogo.static_game import *

def main():
    import bottle
    import os
    view_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'view')
    bottle.TEMPLATE_PATH.insert(0, view_path)

    application = default_app()


    # run(host='localhost', port=8080, reload=True, server='gunicorn', workers=4)
    run(host='localhost', port=8080, reload=True)


@route('/error403')
def error403():
    return template('error403.tpl')


if __name__ == '__main__':
    main()
