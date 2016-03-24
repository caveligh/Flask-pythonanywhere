
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, render_template, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
# Conecciona la BD
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="inticayapy",
    password="MSql2016",
    hostname="inticayapy.mysql.pythonanywhere-services.com",
    databasename="inticayapy$comments",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
db = SQLAlchemy(app)

# Fin DB Conecction
comments = []
# Modelo
class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
# Fin Modelo
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
#        return render_template("main_page.html", comments=comments)
        return render_template("main_page.html", comments=Comment.query.all())

#    comments.append(request.form["contents"])
    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))