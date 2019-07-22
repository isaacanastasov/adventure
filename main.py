import webapp2
import jinja2
import logging
import os
# Step 2 setup the jinja Environment
env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info('Program Ran1')
        # Step 3 Use the jinja Environment to get our file
        template = env.get_template('templates/start.html')
        self.response.write(template.render())

class RunHandler(webapp2.RequestHandler):
    def get(self):
        logging.info('Program Ran2')
        # Step 3 Use the jinja Environment to get our file
        template = env.get_template('templates/run.html')
        self.response.write(template.render())

class GramHandler(webapp2.RequestHandler):
    def get(self):
        logging.info('Program Ran3')
        # Step 3 Use the jinja Environment to get our file
        template = env.get_template('templates/gram.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/run', RunHandler),
    ('/gram', GramHandler),
], debug = True)
