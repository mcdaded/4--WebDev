import json

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import pandas as pd

app = Flask(__name__)
bootstrap = Bootstrap()
bootstrap.init_app(app)

@app.route("/")
def index():
    df = pd.read_csv('data.csv').drop('Open', axis=1)
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
