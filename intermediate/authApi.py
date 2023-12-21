from flask import Flask
from flask_restful import Resource,Api
from flask_httpauth import HTTPBasicAuth

app=Flask(__name__)
api=Api(app)
auth=HTTPBasicAuth()

User_Data={
    'admin':'arpan123'
}

@auth.verify_password
def verify(username,password):
    if not(username and password):
        return False
    return User_Data[username]==password

class privateResource(Resource):
    @auth.login_required
    def get(self):
        return {'hello':'world'}
api.add_resource(privateResource,'/private')
if __name__=='__main__':
    app.run(debug=True,port=5001)