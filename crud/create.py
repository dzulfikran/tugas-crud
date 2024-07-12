import mysql.connector

def create_record(nis, nama_siswa, alamat):
    mysb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_sekolah"
    )

    mycursor = mysb.cursor()

    sql = "INSERT INTO siswa (nis, nama_siswa, alamat) VALUES (%s, %s, %s)"
    val = (nis, nama_siswa, alamat)
    mycursor.execute(sql, val)

    mysb.commit()
    
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mysb.close()
