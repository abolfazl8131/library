

import numpy as np
import pandas as pd
from django.db import connection
from core.models import LoanBook


def test():
    query = str(LoanBook.objects.all().query)
    sql_df = pd.read_sql_table(query , connection)
    return sql_df