NEW_URL="http://gradplanner.us/"
from flask import Flask,redirect
app=Flask(__name__)
@app.route("/",defaults={"path":""})
@app.route("/<path:path>")
def redirectUser(path):
    return redirect(NEW_URL,code=302)
if __name__=='__main__':
    app.run()
