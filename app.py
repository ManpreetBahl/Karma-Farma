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

#=================Start Server========================
app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=8080)
#=====================================================