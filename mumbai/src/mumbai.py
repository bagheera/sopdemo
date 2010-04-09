from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging

class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, from Mumbai!')
        
    def post(self):
        msg = self.request.get('msg')
        origin = self.request.headers.get('Referer', "anon")
        self.response.headers['Content-Type'] = 'text/plain'
        result = 'Mumbai got a msg '+ msg + ' from ' + origin
        logging.info(result)
        self.response.out.write(result)

class HandleScript(webapp.RequestHandler):    
    
    def get(self):
        msg = self.request.get('msg')
        origin = self.request.headers.get('Referer', "anon")
        self.response.headers['Content-Type'] = 'text/javascript'
        result = 'mumbaiCallback("Mumbai got a script msg "+ "'+ msg + ' "+" from "+ "' + origin+'");'
        logging.info(result)
        self.response.out.write(result)
        
application = webapp.WSGIApplication([('/demo', MainPage),('/script', HandleScript)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()