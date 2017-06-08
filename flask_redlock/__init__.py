from redlock import RedLockFactory

__all__ = ('FlaskRedLock', )
__version__ = '0.0.1'


class FlaskRedLock(object):
    def __init__(self, app=None):
        self._redlock_factory = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('REDLOCK_CONNECTIONS', [{'url': 'redis://localhost:6379/0'}, ])

        redlock_connections = app.config['REDLOCK_CONNECTIONS']
        self._redlock_factory = RedLockFactory(connection_details=redlock_connections)

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['redlock_factory'] = self

    def __getattr__(self, name):
        return getattr(self._redlock_factory, name)

    def __getitem__(self, name):
        return self._redlock_factory[name]

    def __setitem__(self, name, value):
        self._redlock_factory[name] = value

    def __delitem__(self, name):
        del self._redlock_factory[name]
