from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging

class Demo(webapp.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, Get from Chennai!')
        
    def post(self):
        msg = self.request.get('msg')
        referer = self.request.headers.get('Referer', "anon")
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.headers['Access-Control-Allow-Origin'] = "http://bangalore.latest.sopdemo.appspot.com"
        result = 'Chennai got a msg '+ msg + ' from ' + referer
        self.response.out.write(result)
    
    def options(self):
        origin = self.request.headers.get('Origin', None)
        logging.info(origin)
        self.response.headers['Access-Control-Allow-Origin'] = "http://bangalore.latest.sopdemo.appspot.com"
        self.response.headers['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS"
        
application = webapp.WSGIApplication([('/demo', Demo)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()