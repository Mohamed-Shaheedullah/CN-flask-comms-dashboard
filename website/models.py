from . import db
import datetime

class Overview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    db_total_income = db.Column(db.Float)
    # db_highest_spend = db.Column(db.Float)
    # db_bestseller = db.Column(db.String(300))
    # db_worstseller = db.Column(db.String(300))
    # db_mvp = db.Column(db.String(300))
    #These arre the columns.