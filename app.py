"""
Copyright 2018 Manpreet Bahl
[This program is licensed under the "MIT License"]
Please see the file LICENSE in the source distribution 
of this software for license terms.
"""
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

#===============Stack Exchange Route==================
@app.route("/stackexchange", methods=["GET", "POST"])
def stackexchange():
    """
    This method handles the GET and POST requests to '/stackexchange'
    endpoint. If the request is a GET, it provides the form where the
    user selects a site on Stack Exchange to get list of questions to
    farm karma. If the request is a POST, it renders the results into
    the appropriate tables based on the filter in the model.
    """
    if request.method == "GET":
        return render_template(presenter.getStackExchange(), sites=app.sites)
    else:
        url, questions = presenter.getNoAnswerQuestions(request.form['site'])
        return render_template(url, sites=app.sites, best=questions[0], good=questions[1], okay=questions[2])
#=====================================================

#===================Reddit Routes=====================
@app.route("/redditaccess", methods=["GET"])
def authReddit():
    """
    This methods provides the OAuth URL for the user to 
    sign in to Reddit to allow access for the application.
    """
    return redirect(presenter.userApproveApp())


@app.route("/reddit", methods=["GET", "POST"])
def getReddit():
    """
    This method renders the user's subscribed subreddits in
    both GET and POST requests. If the request is a POST, it
    also renders the newest posts on the specified subreddit.
    """
    if request.method == "GET":
        return render_template('reddit.html', subreddits=presenter.getUserSubreddits(request.args.get('code')))
    else:
        newPosts = presenter.getSubredditNew(request.form['subreddit'])
        return render_template('reddit.html', subreddits=presenter.getUserSubreddits(code=None), submissions=newPosts)
#=====================================================

#=================Start Server========================
app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=8080)
#=====================================================