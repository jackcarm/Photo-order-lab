from flask import render_template

from app import app
from models.order_list import *


@app.route("/orders")
def index():
    return render_template("index.html", title="Orders", orders=photos)


@app.route("/orders/<index>")
def orders(index):
    return render_template(
        "order_id.html", title="Full Order", order_id=index, orders=photos
    )
