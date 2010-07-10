from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, from Bangalore!')

    def post(self):
        msg = self.request.get('msg')
        origin = self.request.headers.get('Referer', "anon")
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Bangalore got a msg '+ msg + ' from ' + origin)

application = webapp.WSGIApplication([('/demo', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
