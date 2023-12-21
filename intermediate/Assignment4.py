from flask import Flask
from flask_restful import Resource,Api
from flask_httpauth import HTTPBasicAuth
app=Flask(__name__)
api=Api(app)
auth=HTTPBasicAuth()

data=[]

User_Data={
    'admin':'arpan123'
    }

@auth.verify_password
def verify(username,password):
    if not(username and password):
        return False
    return User_Data[username]==password


class Books(Resource):
    @auth.login_required
    def get(self,name):
        for x in data:
            if x['Data']==name:
                return x 
        return {'Data':None}
    @auth.login_required
    def post(self,name):
        temp={'Data':name}
        data.append(temp)
        return temp 
    @auth.login_required
    def delete(self,name):
        for ind,x in enumerate(data):
            if x['Data']==name:
                data.pop(ind)
                return {'Note':'deleted'}
api.add_resource(Books,'/<string:name>')
if __name__=='__main__':
    app.run(debug=True,port=5000)
