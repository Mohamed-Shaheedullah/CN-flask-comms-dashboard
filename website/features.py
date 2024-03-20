from flask import Flask, Blueprint, redirect, render_template, url_for, request
from .models import Overview
from . import db
import pandas as pd

feature = Blueprint("feature", __name__)

@feature.route("/")
def home():
    overview_list = Overview.query.all()    # returns list of objects
    df = pd.DataFrame([(
        i.id,
        i.db_total_income,
        i.db_highest_spend,
        i.db_bestseller,
        i.db_worstseller,
        i.db_mvp

    )for i in overview_list],columns=["id",
                                    "total_income",
                                    "highest_spend",
                                    "best_seller",
                                    "worst_seller",
                                    "mvp_staff"  ])
    # print(overview_list)
    er_message = request.args.get("er_message", None)
    # df = pd.read_sql(Overview.query.all())
    print(df)
    return render_template("home.html", overview_list = overview_list, er_message=er_message)


@feature.route("/add", methods = ["POST", "GET"])
def add():
    try:
        # request form contents by 'name' of form - task
        db_total_income = request.form.get("total_income")
        db_highest_spend = request.form.get("highest_spend")
        db_bestseller = request.form.get("best_selling_item")
        db_worstseller = request.form.get("least_selling_item")
        db_mvp = request.form.get("MVP_staff")

        # left task represents var declared in above line , right task represents contents of form ?
        new_overview = Overview(db_total_income = db_total_income,
                                db_highest_spend=db_highest_spend,
                                db_bestseller= db_bestseller,
                                db_worstseller=db_worstseller,
                                db_mvp=db_mvp
                                )
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
    
@feature.route("/mon")
def mon():
    # overview = Overview.query.all()
    # print(overview)
    return render_template("mon.html")

@feature.route("/tues")
def tues():
    # overview = Overview.query.all()
    # print(overview)
    return render_template("tues.html")

@feature.route("/wed")
def wed():
    # overview = Overview.query.all()
    # print(overview)
    return render_template("wed.html")

@feature.route("/thurs")
def thurs():
    # overview = Overview.query.all()
    # print(overview)
    return render_template("thurs.html")

@feature.route("/fri")
def fri():
    # overview = Overview.query.all()
    # print(overview)
    return render_template("fri.html")

@feature.route("/sat")
def sat():
    # overview = Overview.query.all()
    # print(overview)
    return render_template("sat.html")

@feature.route("/sun")
def sun():
    # overview = Overview.query.all()
    # print(overview)
    return render_template("sun.html")