from flask import Flask, Blueprint, redirect, render_template, url_for, request
from .models import Overview
from . import db
import pandas as pd
import matplotlib.pyplot as plt

feature = Blueprint("feature", __name__)

def base_to_frame(db_query):
    if len(db_query) > 0:
        df = pd.DataFrame([(
            i.id,
            i.db_total_income,
            i.db_highest_spend,
            i.db_bestseller,
            i.db_worstseller,
            i.db_mvp

        )for i in db_query],columns=["id",
                                        "total_income",
                                        "highest_spend",
                                        "best_seller",
                                        "worst_seller",
                                        "mvp_staff"  ])
        return df


@feature.route("/")
def home():
    overview_list = Overview.query.all()    # returns list of objects
    if len(overview_list) > 0:
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
    max_total_income = df['total_income'].max()
    max_highest_spend = df["highest_spend"].max()
    mode_bestseller = df["best_seller"].mode()[0]
    mode_worst_seller = df["worst_seller"].mode()[0]
    mode_mvp_staff = df["mvp_staff"].mode()[0]
    # s = df["total_income"]
    # x = df["id"]
    # plt.scatter(x, s)
    # plt.title("Total Income by Day")
    # plt.xlabel("day")
    # plt.ylabel("Total Income")
    # # plt.show() IS THERE A BETTER WAY OF DOING THIS 
    # plt.savefig('./website/static/my_plot.png')
    return render_template("home.html",
                            max_total_income=max_total_income,
                            max_highest_spend=max_highest_spend,
                            mode_bestseller=mode_bestseller,
                            mode_worst_seller=mode_worst_seller,
                            mode_mvp_staff=mode_mvp_staff,
                            # overview_list = overview_list,
                            er_message=er_message)


@feature.route("/add", methods = ["POST", "GET"])
def add():
    try:
        # request form contents by 'name' of form - task
        db_total_income = request.form.get("total_income")
        db_highest_spend = request.form.get("highest_spend")
        db_bestseller = request.form.get("best_selling_item")
        db_worstseller = request.form.get("least_selling_item")
        db_mvp = request.form.get("MVP_staff")
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
        er_message = "There was an error adding your item"
        return redirect(url_for("feature.home", er_message=er_message))
    
    
@feature.route("/mon")
def mon():
    # mon_income = df["total_income"][0]
    overview = Overview.query.all()
    df = base_to_frame(overview)
    # print(df)
    # print(mon_income)
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