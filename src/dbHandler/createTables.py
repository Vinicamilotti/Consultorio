from sqlite3 import Connection
def createTables(con:Connection, tables:list[str]) -> None:
    qyr = ';'.join(tables)
    con.cursor().execute(qyr)
    con.commit()
    con.close()
          