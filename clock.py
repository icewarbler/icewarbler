## Import datetime modules
from datetime import datetime
from datetime import date  
from datetime import time
from datetime import timedelta
from datetime import tzinfo
from datetime import timezone

## Datetime constructor
##class datetime.datetime(object):
##    def __init__(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

    
today = date.today()

# date object
theDate = date.fromisoformat(date.isoformat(today))
theDateTiem = datetime.now(tz=None)
print("UTC Time:")
print(datetime.now(timezone.utc))
print()
print("Local Time:")
print(datetime.today())
theDateTime = datetime.today()
print(theDateTime)
print(theDateTiem)