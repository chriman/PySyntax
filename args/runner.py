


class Runner(object):
    def __init__(self, http_client_session=None):
        self.http_client_session = http_client_session
        self.context = Context()
