from flask import *
from database1 import Player

# Create a Flask Instance
app = Flask(__name__)


# Create a route decorator which pass Index.html
@app.route("/")
def index():
    return render_template("Index.html")


# This function render Home.html when user click URL /Home
@app.route("/Home")
def home():
    return render_template("Home.html")


# This function render AddPlayers.html when user click URL /AddPlayers
@app.route("/AddPlayers")
def addplayers():
    return render_template("AddPlayers.html")


# This function calls the database function to insert values to the table and
# render AddConfrim.html when user click URL /AddConfrim
@app.route("/AddConfirm", methods=["POST"])
def addconfirm():
    message = "Player Data Inserted"

    if request.method == "POST":
        formdata = request.form
        try:
            play.insertplayer(formdata)  # call DB to handle insertion
        except Exception:
            message = "Data Incorrect, Please insert correct player ID"

    return render_template("AddConfirm.html", insertmessage=message)


# This function calls the database function to display the inserted values from table and
# render ViewPlayers.html when user click URL /ViewPlayers
@app.route("/ViewPlayers")
def viewplayers():
    playerdata = play.allplayers()  # call DB to handle display
    return render_template("ViewPlayers.html", data=playerdata)


# This function calls the database function to display a particular data with id and
# render PlayerUpdate.html when user click URL /PlayerUpdate
@app.route("/PlayerUpdate/<int:id>")
def playerupdate(id):
    playerdata = play.retrieveplayer(id)[0]  # call DB to handle display
    return render_template("PlayerUpdate.html", data=playerdata)


# This function calls the database function to update the values in table and
# render ViewPlayers.html when user click URL /UpdatePlayer
@app.route("/UpdatePlayer", methods=["POST"])
def updateplayer():
    if request.method == "POST":
        formdata = request.form
        play.updateplayer(formdata)

    playerdata = play.allplayers()  # call DB to handle updation
    return render_template("ViewPlayers.html", data=playerdata)


# This function calls the database function to delete the values in table and
# render ViewPlayers.html when user click URL /PlayerDelete
@app.route("/PlayerDelete/<int:id>")
def playerdelete(id):
    play.deleteplayerdata(id)
    playerdata = play.allplayers()  # call DB to handle deletion
    return render_template("ViewPlayers.html", data=playerdata)


# This function is to handle Invalid URL
@app.errorhandler(404)
def page_not_found(notfound):
    return render_template("404.html"), 404


# This function is to handle Internal Server Error
@app.errorhandler(500)
def page_not_found(notfound):
    return render_template("500.html"), 500

# This function is to connect the page database.py and the database player.db
if __name__ == "__main__":
    DbName = "./database/players.db"  # Database Name

    play = Player(DbName)  # New player object
    play.createdbt()  # DB and Table creation
    app.run(debug=True)
