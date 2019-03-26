import falcon

from malfoy import db


class RootResource:
    def on_get(self, request, response):
        result = db.query("SELECT NOW() AS now;")
        response.status = falcon.HTTP_200
        response.media = {
            'app': 'tunedmystic-tests',
            'params': request.params,
            'now': result[0]['now'].strftime('%c')
        }


def get_api():
    app = falcon.API()
    app.add_route('/', RootResource())
    return app


def get_app():
    db.init()
    return get_api()
