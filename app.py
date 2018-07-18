#======================Imports========================
from flask import Flask, render_template, request, redirect, url_for

from model import AppModel
from presenter import Presenter
#=====================================================

#======================Setup==========================
app = Flask(__name__)
model = AppModel(app)
presenter = Presenter(model)
#=====================================================

#====================Home Route=======================
@app.route("/")
def home():
    return render_template(presenter.home())
#=====================================================

#====================Home Route=======================
@app.route("/stackexchange", methods=["GET", "POST"])
def stackexchange():
    siteURL, sites = presenter.getStackExchange()
    return render_template(siteURL, sites=sites)
#=====================================================

#=================Start Server========================
app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=8080)
#=====================================================