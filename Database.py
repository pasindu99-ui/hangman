# This is for check data connectivity

def hangman_db():
    import mysql.connector
    from mysql.connector import Error
    my_db = mysql.connector.connect(host="localhost",user="root", passwd="")
    try:
        if my_db.is_connected():
            print("Connected successfully.")
            new_cursor = my_db.cursor()
            new_cursor.execute("CREATE DATABASE IF NOT EXISTS Thilini_20200476;")
    except Error as e:
        print("Something went wrong", e)

#This function is creating a database name calling as thilini_20200476 
def hangman_db_table():
    import mysql.connector
    from mysql.connector import Error
    my_table_conn = mysql.connector.connect(host="localhost", user="root", passwd="",database="Thilini_20200476")
    try:
        if my_table_conn.is_connected():
            print("Connected successfully.")
            table_cursor = my_table_conn.cursor()
            table_cursor.execute("CREATE TABLE IF NOT EXISTS game_play(player_name VARCHAR(50), word VARCHAR(25), turns_provided INT, turns_used INT,  status VARCHAR(15))")
    except Error as e:
        print("Something went wrong", e)


def insert_data(name,word,turns_provide,turn_used,status):
    import mysql.connector
    from mysql.connector import Error
    add_data_conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Thilini_20200476")
    try:
        if add_data_conn.is_connected():
            print("Connected successfully.")
            data_cursor = add_data_conn.cursor()
            add_command ="INSERT INTO game_play(player_name, word, turns_provided , turns_used  , status) VALUES (%s,%s,%s,%s,%s)"
            insert_params = (name,word,turns_provide,turn_used,status)
            data_cursor.execute(add_command, insert_params)
            print(data_cursor.rowcount,"added the record")
            add_data_conn.commit()
    except Error as e:
        print("Something is wrong", e)

def display_data():
    import mysql.connector
    add_data_conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="Thilini_20200476")
    #get all the records from the database
    print("\n----History----\n")
    data_cursor = add_data_conn.cursor()
    data_cursor.execute("SELECT * FROM game_play")
    myresult = data_cursor.fetchall()
    for x in myresult:
        for i in x:
            print(i,end="     ")
        print()
   




hangman_db()
hangman_db_table()


