from pyramid.response import Response
from pyramid.view import (
    view_config,
    view_defaults
    )

from sqlalchemy.exc import DBAPIError

from .models.meta import DBSession
from .models import User


@view_defaults(renderer='templates/howdy.jinja2')
class HowdyViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='howdy')
    def howdy(self):
        first = self.request.matchdict['first']
        last = self.request.matchdict['last']
        return {
            'page': 'Howdy View',
            'first': first,
            'last': last
        }

@view_config(route_name='home', renderer='templates/home.jinja2')
def my_view(request):
    try:
        dave = DBSession.query(User).filter(User.name == 'dave').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'user': dave.name, 'page': 'Basic View'}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_starter_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

