import os

import logging
from flask import Flask

logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
   logger.info(f'Starting app in dev environment')
   app = Flask(__name__)
#    api.init_app(app)
#    db.init_app(app)

   # define hello world page

   @app.route('/')
   def index():
       return 'Message from the backend: "It works!"'
   return app


if __name__ == "__main__":
   app = create_app()
   app.run(host='0.0.0.0', debug=True)