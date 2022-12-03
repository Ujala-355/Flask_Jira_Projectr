from flask import Flask, render_template
from flask_mysqldb import MySQL


app=Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="Ujala123@"
app.config["MYSQL_DB"]="tickets_data"

mysql=MySQL(app)

@app.route('/') 
def flask_fun():
    cur=mysql.connection.cursor()
    cur.execute("SELECT *FROM mysql_data")
    fetchdata=cur.fetchall()
    cur.close()
    return render_template("index.html",fetchdata=fetchdata)

if __name__ == "__main__":
    app.run(debug=True)