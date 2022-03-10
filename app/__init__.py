from flask import render_template, Flask
from dynamoDB_access import get_item_by_attribute

app = Flask(__name__)


@app.get('/')
def index():
    total = 0
    readings = get_item_by_attribute("Unit", "GPS_tracker2")
    for dist in readings:
        total += dist['Distance traveled']
    return render_template('index.html', readings=readings, total=total)
