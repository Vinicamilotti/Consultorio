import os
from .createTables import createTables
from .connect import connection
from .tableList import tableList

createTables(connection(), tableList())
