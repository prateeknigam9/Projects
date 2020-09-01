from flask import Flask,render_template,request
import mysql.connector
import json

#connect the mysql
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Mumbai@143"
)

app= Flask(__name__)

#list of databases and tables
db_name_list=[]
tb_name_list=[]

#listing the database
global dbcursor
dbcursor = db.cursor()
dbcursor.execute("SHOW DATABASES")
for database in dbcursor:
    db_name_list.append(database[0])
db_created_only = db_name_list[:2] #Only the databases created and not the defaults


def fetching(selected_db,selected_tables,cursor):
    cursor.execute("SELECT * FROM "+str(selected_tables))
    result = cursor.fetchall()
    
    return result


#main page
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Database selector',
                           db_list=db_created_only,
                        )

@app.route("/select_table" , methods=['GET', 'POST'])
def select_table():
    global selected_db
    selected_db = request.form.get('database_selected')

    tb_name_list=[]
    dbcursor.execute("USE "+str(selected_db))
    dbcursor.execute("SHOW TABLES")
    for tables in dbcursor:
        tb_name_list.append(tables[0])

    return render_template("select_table.html",
                           title='table selector',
                           db_name=selected_db,
                           tb_list=tb_name_list)

@app.route("/final_output" , methods=['GET', 'POST'])
def final():
    tables = request.form.get('table_selected')
    
    output = fetching(selected_db,tables,dbcursor)

    return json.dumps(dict(output))





app.run(debug=True)