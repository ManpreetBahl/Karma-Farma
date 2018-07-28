#======================Imports========================
from flask import Flask, render_template, request, redirect, url_for, jsonify

from model import AppModel
from presenter import Presenter
#=====================================================

#======================Setup==========================
app = Flask(__name__)
model = AppModel(app)
presenter = Presenter(model)
app.sites = presenter.getSites()
#=====================================================

#====================Home Route=======================
@app.route("/")
def home():
    return render_template(presenter.home())
#=====================================================

#====================Stack Exchange Route=======================
@app.route("/stackexchange", methods=["GET", "POST"])
def stackexchange():
    if request.method == "GET":
        return render_template(presenter.getStackExchange(), sites=app.sites, questions=None)
    else:
        url, questions = presenter.getNoAnswerQuestions(request.form['site'])
        return render_template(url, sites=app.sites, questions=questions)

#=====================================================

#=================Start Server========================
app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=8080)
#=====================================================