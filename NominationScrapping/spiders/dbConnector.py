import psycopg2


def getConnection():
    con = psycopg2.connect(database="oinp", user="postgres", password="harshit24", host="127.0.0.1", port="5432")
    return con

def addDate(dateString):
    con = getConnection()
    cur = con.cursor()
    cur.execute("INSERT INTO statusTable (dateString,emailFlag) values ('%s',%s)" % (dateString, True))
    con.commit()
    cur.close()
    con.close()

def checkForEmail(dateString):
    con = getConnection()
    cur = con.cursor()
    cur.execute("SELECT * from statusTable where dateString = '%s'" % (dateString,))
    rows = cur.fetchall()
    if len(rows) == 0:
        addDate(dateString)
        con.close()
        return False
    else:
        con.close()
        return True


