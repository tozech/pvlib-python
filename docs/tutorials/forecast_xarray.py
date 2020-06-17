#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 22:20:02 2020

@author: tzech
"""
import xarray as xr
import pandas as pd
from pvlib import forecast

m = forecast.GFS()
start = pd.Timestamp.now(tz='UTC')
end = start + pd.Timedelta(days=1)
d = m.get_data(48., 7.8, start, end, outformat='xarray')

