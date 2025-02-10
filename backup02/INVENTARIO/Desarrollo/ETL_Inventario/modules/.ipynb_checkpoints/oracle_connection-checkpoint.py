import pandas as pd
import oracledb
from sqlalchemy import create_engine

def set_engine(db_parameters=None):

    if db_parameters == None:
        engine = create_engine('sqlite:///db_test.sqlite')
    
    else:

        username = db_parameters['user']
        password = db_parameters['password']
        host = db_parameters['host']
        port = db_parameters['port']
        service_name = db_parameters['s_name']
        thick_mode = {}
            
        # print(f'oracle+oracledb://{username}:{password}@{host}:{port}/?service_name={service_name}')

        engine = create_engine(
            f'oracle+oracledb://{username}:{password}@{host}:{port}/?service_name={service_name}',
            thick_mode=thick_mode)

    return engine

