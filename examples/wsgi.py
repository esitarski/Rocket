# -*- coding: utf-8 -*-

import logging
from wsgiref.simple_server import demo_app
from rocket import Rocket

if __name__ == '__main__':
    log = logging.getLogger('Rocket')
    log.setLevel(logging.DEBUG)
    fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
    h = logging.StreamHandler()
    h.setFormatter(fmt)
    log.addHandler(h)
    
    app_info = dict(wsgi_app=demo_app)
    Rocket(interfaces=[('127.0.0.1', 80)],
           method='wsgi',
           app_info=app_info).start()
