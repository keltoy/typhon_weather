from tornado import gen, web
from .BaseHandler import BaseHandler

class HomeHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        """
        delay = self.get_argument('delay', 5)
        yield gen.sleep(int(delay))
        self.write({"status": 1, "msg":"oh success"})
        self.finish()
        """
        self.redirect("/propagation/北京", permanent=True)
