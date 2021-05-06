
import sqlalchemy
from conf.connexion import mysql_pseudo, mysql_mdp

def mysql_connect():
    """function to connect to the database """
    mysql_username = mysql_pseudo
    mysql_password = mysql_mdp
    database_name = 'airbnb'
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@localhost/{2}'.format(mysql_username, mysql_password, database_name), pool_recycle=1, pool_timeout=57600).connect()
    return database_connection

def save_to_mysql(db_connect,df_to_save,df_name):
    """function to import data from file into database """
    df_to_save.to_sql(con=db_connect, name=df_name, if_exists='replace')