#Creating multiple databases and mutiple lists
import mysql.connector
import numpy as np

#Creating multiple databases as according to the list Named database_Name
database_name  = ['DB1','DB2']

#Table details for database1 and database2
table_dict = { 
    "Table_Title_db1" : (['I_and_D_db1','CIS_db1','DSA_db1','BIGDATA_db1','CLOUD_db1'],['col1_db1','col2_db1']),
    "Table_Title_db2" : (['I_and_D_db2','CIS_db2','DSA_db2','BIGDATA_db2','CLOUD_db2'],['col1_db2','col2_db2'])
}

def n_tables(Table_Title,columns,database):
    '''
    Creating Multiple tables as according to the list of Table titles
    '''
    print("Creating tables for database : ",database)
    db_connect = 0
    db_connect = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Mumbai@143",
        database = str(database)
    )
    for table in Table_Title:
        table_cursor = db_connect.cursor()
        table_cursor.execute("CREATE TABLE "+ str(table) +" (" + str(columns[0]) + " VARCHAR(255), " + str(columns[1]) +" INTEGER(255))")
        print(".",end="")
        formula = "INSERT INTO "+ str(table) + "(" + str(columns[0]) + ", " + str(columns[1])+") VALUES (%s,%s)"
        data = [('a_'+str(table),np.random.randint(0,100)),
                ('b_'+str(table),np.random.randint(0,100)),
                ('c_'+str(table),np.random.randint(0,100)),
                ('d_'+str(table),np.random.randint(0,100)),
                ('e_'+str(table),np.random.randint(0,100)),
                ('f_'+str(table),np.random.randint(0,100))
                ]
        table_cursor.executemany(formula,data)
        print(".",end="")
    db_connect.commit()
    print("Tables created")

db = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    passwd = 'Mumbai@143'
) 

for i,db_name in enumerate(database_name):
    try:
        main_cursor = db.cursor()
        main_cursor.execute("CREATE DATABASE " + str(db_name))
        print("Database_Created : ",db_name)

        key=list(sorted(table_dict.keys()))[i]
        table_name = list(table_dict[key][0])
        column_name = list(table_dict[key][1])

        n_tables(table_name,column_name,db_name)
        
    except:
        print("db and table already exists")
        pass

db.commit()