from utils import StringBuilder
def tableList() -> list[str]:
    tabelas = []
    strSql = StringBuilder()

    strSql.clear()
    strSql.append(' CREATE TABLE IF NOT EXISTS RESPONSAVEL (             ');
    strSql.append('     ID_RESPONSAVEL INTEGER PRIMARY KEY AUTOINCREMENT,');
    strSql.append('     NOME_COMPLETO TEXT,                              ');
    strSql.append('     CONTATO TEXT,                                    ');
    strSql.append('     CPF TEXT                                         ');
    strSql.append(' )                                                    ');

    strSql.clear()
    strSql.append(' CREATE TABLE IF NOT EXISTS PACIENTES (                       ');
    strSql.append('     ID_PACIENTE INTEGER PRIMARY KEY AUTOINCREMENT,           ');
    strSql.append('     ID_RESPONSAVEL INTEGER,                                  ');
    strSql.append('     NOME_COMPLETO TEXT,                                      ');
    strSql.append('     CONTATO TEXT,                                            ');
    strSql.append('     CPF VARCHAR(255),                                        ');
    strSql.append('     TPADULTO INTEGER DEFAULT (0),                            ');
    strSql.append('     CONSTRAINT RESPONSAVEL_FK FOREIGN KEY (ID_RESPONSAVEL)   ');
    strSql.append('     REFERENCES RESPONSAVEL(ID_RESPONSAVEL)                   ');
    strSql.append(' )                                                            ');
    tabelas.append(strSql.toString())


    tabelas.append(strSql.toString())
    
    
    return tabelas

