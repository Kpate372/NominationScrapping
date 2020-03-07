import psycopg2


def getConnection():
    con = psycopg2.connect(database="oinp", user="postgres", password="harshit24", host="127.0.0.1", port="5432")
    return con


def addDate(dateString, noOfTimes):
    con = getConnection()
    cur = con.cursor()
    cur.execute("INSERT INTO statusTable (dateString,emailFlag,noOfTimes) values ('%s',%s, %d)" % (dateString, True, noOfTimes))
    con.commit()
    cur.close()
    con.close()


def updateDate(dateString, newCount):
    con = getConnection()
    cur = con.cursor()
    cur.execute("UPDATE statusTable SET noOfTimes =  %d where dateString ='%s'" % (newCount, dateString))
    con.commit()
    cur.close()
    con.close()


def checkForEmail(dateString, noOfTimes):
    con = getConnection()
    cur = con.cursor()
    cur.execute("SELECT * from statusTable where dateString = '%s'" % (dateString,))
    rows = cur.fetchone()
    if rows == None:
        addDate(dateString, 1)
        con.close()
        return False
    else:
        currentCount = rows[2]
        if currentCount != noOfTimes:
            updateDate(dateString, currentCount + 1)
            con.close()
            return False
        else:
            con.close()
            return True


