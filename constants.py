from datetime import datetime, timedelta
import radar
import random


class Constants:
    TODAY = datetime.today().strftime("%Y-%m-%d")
    TOMORROW = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    YESTERDAY = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    RANDOM_DATE_VALID_1 = radar.random_datetime(start='1995-06-16', stop='1997-12-31').strftime("%Y-%m-%d")
    RANDOM_DATE_VALID_2 = (datetime.strptime(RANDOM_DATE_VALID_1, "%Y-%m-%d") \
                           + timedelta(days=random.randint(1, 400))).strftime("%Y-%m-%d")
    RANDOM_DATE_FUTURE = radar.random_datetime(start=TOMORROW, \
                                stop=((datetime.strptime(TOMORROW, "%Y-%m-%d")+ \
                                      timedelta(days=random.randint(1, 400))).strftime("%Y-%m-%d"))).strftime("%Y-%m-%d")
    RANDOM_DATE_FUTURE_2 = (datetime.strptime(RANDOM_DATE_FUTURE, "%Y-%m-%d") \
                            + timedelta(days=random.randint(1, 400))).strftime("%Y-%m-%d")
    RANDOM_DATE_PAST = radar.random_datetime(stop='1995-06-15').strftime("%Y-%m-%d")
    RANDOM_DATE_PAST_2 = (datetime.strptime(RANDOM_DATE_PAST, "%Y-%m-%d") \
                          + timedelta(days=random.randint(1, 400))).strftime("%Y-%m-%d")
    RANDOM_NUMBER = random.randint(1, 100)
    RANDOM_NUMBER_INVALID = random.randint(101, 200)
    RANDOM_NUMBER_INVALID_NEG = random.randint(-100, 0)