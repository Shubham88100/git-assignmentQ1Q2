from flask import Flask, redirect, render_template , request
from dotenv import load_dotenv 
import os
import pymongo


load_dotenv()

MONGO_URI=os.getenv('MONGO_URI')

client=pymongo.MongoClient(MONGO_URI)
db=client.test
collection = db['flask-assignments']
app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def form():
    error=""
    
    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        
        if not name or not email:
            error="Name or email required"
            return render_template("index.html",error=error)
        try:
            collection.insert_one({
                "name":name,
                "email":email
            })
            
            return redirect("/success")
        
        except Exception as e:
            error=str(e)
    return render_template("index.html",error=error)

@app.route('/success')
def success():
    return "Data submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)