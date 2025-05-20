from app import app, db
from models import Meter, MeterData
from faker import Faker
import random

fake = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    for i in range(5):
        meter = Meter(label=f"Meter {i + 1}")
        db.session.add(meter)
        db.session.commit()

        for _ in range(10):
            db.session.add(MeterData(
                meter_id=meter.id,
                timestamp=fake.date_time_this_year(),
                value=random.randint(0, 100)
            ))

    db.session.commit()