import pyodbc
import pandas as pd


server = "172.16.200.70"
bd ="MA02-SCEP2016_BTDATA"
user ="supercep"
password = "PASSWORD"

try:

    conexion = pyodbc.connect("DRIVER={OBDC Driver 17 for SQL server};SERVER ='+server+';DATABASE = '+bd+';UID='+user+' ;PWD='+password'")
    print("Conexion Exitosa")

except:                          
    print("Conexion Fallida")

