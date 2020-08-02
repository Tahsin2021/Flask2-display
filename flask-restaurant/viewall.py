from flask import *
import sqlite3


app = Flask(__name__)

@app.route("/")
def main():
    # make a connection to the database
    db = sqlite3.connect('restaurant.db')
    cursor = db.cursor()
    # make a query to return all items
    myList = cursor.execute("SELECT * FROM menu").fetchall()
    # I like to do print statements to see how my data returns
    print(myList)
    
    # I'm not making any changes to the database, so no need to commit
    # I do need to close the connection though
    db.close()
    return render_template('list.html', myList=myList)

app.run(debug=True)
