from flask import Flask, Blueprint, redirect, render_template, url_for, request
from .models import Overview
from . import db

feature = Blueprint("feature", __name__)

@feature.route("/")
def home():
    overview_list = Overview.query.all()    # returns list of objects
    print(overview_list)
    er_message = request.args.get("er_message", None)
    return render_template("home.html", overview_list = overview_list, er_message=er_message)


@feature.route("/add", methods = ["POST", "GET"])
def add():
    try:
        # request form contents by 'name' of form - task
        db_total_income = request.form.get("total_income")
        # left task represents var declared in above line , right task represents contents of form ?
        new_overview = Overview(db_total_income = db_total_income)
        db.session.add(new_overview)
        db.session.commit()
        return redirect(url_for("feature.home"))
    except:
        er_message = "There was an error adding your task"
        return redirect(url_for("feature.home", er_message=er_message))
    
# @feature.route("/read")
# def read():
#     overview_list = Overview.query.all()    # returns list of objects
#     print(overview_list)
#     er_message = request.args.get("er_message", None)
#     return render_template("home.html", overview_list = overview_list, er_message=er_message)