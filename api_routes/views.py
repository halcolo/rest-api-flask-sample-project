from flask import jsonify
from flask.views import MethodView

class HelloWorldView(MethodView):
    """return Hello world message

    Args:
        MethodView (_type_): _description_
    """
    def get(self):
        return jsonify({"message": "Hello, world!"})
    

