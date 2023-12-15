from flask import flask, Blueprint
from flask_restplus import Api

class Server():
    def __init__(self,):
        self.app = flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc = '/doc', title= 'SQLAlchemy ORM')
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///5sbd.db'
        self.app.config['PROPAGATE_EXCEPTIONS']= True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

        self.book_ns = self.book_ns()

    def book_ns(self,):
        return  self.api.namespace(name='Books', description='books related operations', path='/')

    def run(self,):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )

server = Server()