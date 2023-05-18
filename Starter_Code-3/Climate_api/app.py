 
# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,MetaData, func, select
from flask import Flask
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()

Base.prepare(autoload_with=engine)
# reflect the tables
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app=Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route('/')
def avaliable_routes():
    return '''
    /api/v1.0/precipitation\n
    /api/v1.0/stations\n
    /api/v1.0/tobs\n
    /api/v1.0/<start>\n
    /api/v1.0/<start>/<end>\n'''
@app.route( '/api/v1.0/precipitation')
def get_precipitation():
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_yr).all()
    print(results)
app.run()