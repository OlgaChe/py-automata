import uuid
import datetime
import json


# generate unique uuid
def generate_uuid():
    driver_id = str(uuid.uuid4())
    print(driver_id)


def generate_date_time():
    # create unique driver id
    id_date = "test_qa_" + datetime.datetime.now().strftime('%m%d%H%M')
    print(id_date)


generate_uuid()
generate_date_time()
