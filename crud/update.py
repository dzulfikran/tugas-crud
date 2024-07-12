import mysql.connector

def update_record(nis, nama_siswa, alamat ):
    try:
        mysb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_sekolah"
        )

        mycursor = mysb.cursor()

        sql = "UPDATE siswa SET nis = %s, nama_siswa = %s, alamat = %s WHERE nis = %s"
        val = (nis, nama_siswa, alamat, nis)
        print("Executing SQL:", sql % val)  # Debug statement
        mycursor.execute(sql, val)

        mysb.commit()
        
        print(mycursor.rowcount, "record(s) affected")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        mycursor.close()
        mysb.close()

# Example usage
