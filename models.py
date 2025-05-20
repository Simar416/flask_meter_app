from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Meter(db.Model):
    __tablename__ = 'meters'
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String, nullable=False)
    data = db.relationship('MeterData', backref='meter', lazy=True)

class MeterData(db.Model):
    __tablename__ = 'meter_data'
    id = db.Column(db.Integer, primary_key=True)
    meter_id = db.Column(db.Integer, db.ForeignKey('meters.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    value = db.Column(db.Integer, nullable=False)


