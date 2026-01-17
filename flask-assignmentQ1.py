from flask import Flask,request,jsonify
from data import users

app=Flask(__name__)

@app.route('/api')
def api():
   
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
    