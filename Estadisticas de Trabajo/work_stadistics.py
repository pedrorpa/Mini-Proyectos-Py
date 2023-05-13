import datetime as dt
import os
import zoneinfo

import pandas as pd

TIMEZONE = zoneinfo.ZoneInfo(os.getenv("TIMEZONE", "Atlantic/Canary"))


def fecha_modificacion(filename):
    n_secs = os.path.getmtime(filename)
    time = dt.datetime.fromtimestamp(n_secs)
    return time.strftime("%Y-%m-%d")


def fecha_creacion(filename):
    n_secs = os.path.getctime(filename)
    time = dt.datetime.fromtimestamp(n_secs)

    return time.strftime("%Y-%m-%d")


def fecha_ultima_semana():
    now = dt.datetime.now()
    delta_week = dt.timedelta(days=7)
    return (now - delta_week).strftime("%Y-%m-%d")


date_now = dt.datetime.now().strftime("%Y-%m-%d")
for entry in os.listdir():
    if os.path.isfile(entry) or os.path.isdir(entry):
        fecha_mod = fecha_modificacion(entry)
        print(
            f"Modificados desde {fecha_ultima_semana()} hasta el {fecha_modificacion(entry)}"
        )

        print(f"{entry:>24} {fecha_mod:19} \u2589")
        print(" ")
    else:
        print(f"{entry:>24}/")

actual_day = dt.datetime.now().day
last_seven_days = fecha_ultima_semana()
