from datetime import datetime, timedelta, timezone
from opentelemetry import trace
# import logging

from lib.db import db

tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(
    # logger # (method 1)
    cognito_user_id=None
  ):
    # LOGGER = logging.getLogger(__name__) # (method 2)
    # LOGGER.info("homeActivities") # (method 2)
    # logger.info("homeActivities") # (method 1)
    with tracer.start_as_current_span("home-activities-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      
      sql = db.template("activities", "home")
      results = db.query_array_json(sql)
      return results
  
