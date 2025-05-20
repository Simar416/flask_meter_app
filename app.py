from flask import Flask, render_template, jsonify
from models import db, Meter, MeterData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/meters/')
def get_meters():
    meters = Meter.query.all()
    return render_template('meters.html', meters=meters)

@app.route('/meters/<int:meter_id>')
def get_meter_data(meter_id):
    data = MeterData.query.filter_by(meter_id=meter_id).order_by(MeterData.timestamp).all()
    return jsonify([
        {'id': d.id, 'timestamp': d.timestamp.isoformat(), 'value': d.value}
        for d in data
    ])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)