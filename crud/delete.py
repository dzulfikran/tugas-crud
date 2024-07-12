import mysql.connector

def delete_record(nis):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_sekolah"
    )

    mycursor = mysb.cursor()

    sql = "DELETE FROM siswa WHERE nis = %s"
    val = (nis,)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record(s) deleted")

    mycursor.close()
    mysb.close()
