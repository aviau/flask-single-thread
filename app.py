import datetime
import time

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_get():

    time_start = datetime.datetime.now()

    time.sleep(10)

    time_end = datetime.datetime.now()

    return render_template(
        "index.html",
        time_start=time_start,
        time_end=time_end,
    )
