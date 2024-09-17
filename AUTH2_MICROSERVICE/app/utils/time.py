from datetime import datetime
import pytz

def get_current_datetime():
    utc_now = datetime.utcnow().replace(microsecond=0)
    utc_now = utc_now.replace(tzinfo=pytz.utc)
    timezone = pytz.timezone('Asia/Kolkata')
    local_time = utc_now.astimezone(timezone)
    local_time_naive = local_time.replace(tzinfo=None)
    return local_time_naive