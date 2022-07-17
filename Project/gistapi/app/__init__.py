from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery
import sched, time, subprocess

s = sched.scheduler(time.time, time.sleep)
def cache_clear(sc):
    print('clearing cache...')
    rc = subprocess.call('/home/sema/gistapi/clear_db.sh')
    sc.enter(60, 1, cache_clear, (sc,))

s.enter(60, 1, cache_clear, (s,))
s.run()


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models