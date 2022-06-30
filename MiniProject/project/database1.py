"""This module implements Database related things"""
import sqlite3


# Implementation of Object Orientation Programming
class Player:
    def __init__(self, DBName):
        self.DbName = DBName

    # Database Table Creation
    def createdbt(self):
        conn = sqlite3.connect(self.DbName)
        cursor = conn.cursor()
        query1 = f"""CREATE TABLE IF NOT EXISTS FOOTBALLPLAYERS(ID INT PRIMARY KEY NOT NULL, 
                            NAME CHAR(30) NOT NULL,
                            CLUB CHAR(18),
                            NATIONALITY CHAR(15),
                            POSITION CHAR(5),
                            AGE INT(2) )"""
        cursor.execute(query1)
        conn.commit()
        conn.close()

    # Inserting values to the Table when user click submit button in AddPlayers.html
    def insertplayer(self, formdata):
        id = int(formdata["plyid"])
        name = formdata["plyname"]
        club = formdata["plyclub"]
        nationality = formdata["plynatio"]
        position = formdata["plyposi"]
        age = formdata["plyage"]

        conn = sqlite3.connect(self.DbName)
        conn.execute(
            "INSERT INTO FOOTBALL_PLAYERS (ID,NAME,CLUB,NATIONALITY,POSITION,AGE) "
            f"VALUES ({id}, '{name}', '{club}', '{nationality}', '{position}', '{age}')"
        )
        conn.commit()
        conn.close()

    # Displaying the inserted values from table when user click ViewPlayer.html
    def allplayers(self):
        conn = sqlite3.connect(self.DbName)
        cursor = conn.execute("SELECT * FROM FOOTBALL_PLAYERS ORDER BY ID")
        playerdata = cursor.fetchall()
        conn.commit()
        conn.close()
        return playerdata

    # Displaying the values of a particular id when user click on update option in the ViewPlayers.html
    def retrieveplayer(self, id):
        conn = sqlite3.connect(self.DbName)
        cursor = conn.execute(f"SELECT * from FOOTBALL_PLAYERS WHERE ID={id}")
        playersdata = cursor.fetchall()
        conn.commit()
        conn.close()
        return playersdata

    # update the value in table when user click on submit button in PlayerUpdate.html
    def updateplayer(self, formdata):
        id = formdata["plyid"]
        name = formdata["plyname"]
        club = formdata["plyclub"]
        nationality = formdata["plynatio"]
        position = formdata["plyposi"]
        age = formdata["plyage"]

        conn = sqlite3.connect(self.DbName)
        conn.execute(
            f"UPDATE FOOTBALL_PLAYERS SET ID={id}, NAME='{name}', CLUB='{club}', "
            f"NATIONALITY='{nationality}', POSITION='{position}', AGE='{age}' WHERE ID={id}"
        )
        conn.commit()
        conn.close()
        print("Data updateded")

    # Delete the value from table when user click delete option in ViewPlayer.html
    def deleteplayerdata(self, id):
        conn = sqlite3.connect(self.DbName)
        conn.execute(f"DELETE FROM FOOTBALL_PLAYERS WHERE ID={id}")
        conn.commit()
        conn.close()
