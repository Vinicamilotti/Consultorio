from utils import StringBuilder
def tableList() -> list[str]:
    tabelas = []
    strSql = StringBuilder()
    
    strSql.clear()
    strSql.append(' CREATE TABLE IF NOT EXISTS PACIENTES (               ');
    strSql.append('     ID_PACIENTE INTEGER PRIMARY KEY AUTOINCREMENT,   ');
    strSql.append('     NOME_COMPLETO VARCHAR(255),                      ');
    strSql.append('     TPADULTO INTEGER DEFAULT (0)                     ');
    strSql.append(' )                                                    ');
    tabelas.append(strSql.toString())
    
    
    return tabelas