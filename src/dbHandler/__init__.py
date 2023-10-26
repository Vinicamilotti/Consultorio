from .tableList import tableList
from .dbModule import DBModule

db = DBModule()
db.createTables(tableList())
db.closeConnection()
