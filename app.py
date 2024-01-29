# Import the dependencies
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

#################################################
# Database Setup
#################################################

# Create engine to connect to SQLite database
#engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
#Base.prepare(engine, reflect=True)

# Save references to each table
#Measurement = Base.classes.measurement
#Station = Base.classes.station

# Create our session (link) from Python to the DB
#session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Welcome page with available routes
@app.route("/")
def home():
    return (
        f"Welcome to the Climate Analysis API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

    session.close()

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
