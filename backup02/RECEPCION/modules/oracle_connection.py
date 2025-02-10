import oracledb
from os import getenv

# Return True if object type is a list of tuples. Otherwise raise TypeError
# records: Object
def check_records_is_list_of_tuples(records):

    data_type = type(records)

    if data_type is list:
        for element in records:
            if isinstance(element, tuple)==False:
                return False
                # raise TypeError("Todos los elementos de la lista deben ser de tipo tupla.")
        return True
    
    else:
        raise TypeError("El tipo de objeto debe ser una lista.")

class Oracle_Conection():
    def __init__(self, user, password, host, port, s_name):
        self.user = user
        self.password = password
        self.host = host
        self.port= port
        self.s_name = s_name
        
    def Connect(self):
        oracledb.init_oracle_client(lib_dir=None)
        params = oracledb.ConnectParams(host=self.host, port=self.port, service_name=self.s_name)
        self.conn = oracledb.connect(user=self.user, password=self.password, params=params)
        # print("Se ha conectado correctamente..")
        
    def Execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        print("Query ejecutado correctamente..")

    def Create_Table(self, table_name, fields):
        # table_name: string
        # fiedls: dictionary; {fieldNname: dataType}

        query = "CREATE TABLE " + table_name + " ("
        for key in fields:
            query += key + " " + fields[key] + ", "
        
        query = query[0:-2] + ")"
        self.cursor.execute(query)

        print("La tabla {} ha sido creada exitosamente..".format(table_name))
        self.conn.commit()

    def Create_Table_As(self, table_name, query_table):
        query = "CREATE TABLE " + table_name + " AS (" + query_table + ")"
        self.cursor.execute(query)

        print("La tabla {} ha sido creada exitosamente..".format(table_name))
        self.conn.commit()


    def Insert_Rows(self, table_name, record_names, records):
        # table_name: string
        # record_names: list
        # records: tuple List

        if isinstance(record_names, list)==False:
            raise TypeError("El objeto record_names debe ser una lista")
        else:
            record_names_string=""
            for name in record_names:
                record_names_string += name + ", "
            
            record_names_string= record_names_string[:-2]


        if check_records_is_list_of_tuples(records):
            values_string = ""
            for i in range(1, len(records[0])+1):
                values_string += ":" + str(i) + ", "
            values_string = values_string[:-2]

            query = "insert into {} ({}) values({})".format(table_name, record_names_string, values_string)
            print(query)
            print(records)
        
        else:
            query = "insert into {} ({}) values(:1)".format(table_name, record_names_string)

    def Close(self):
        self.conn.close()
        print("Se ha cerrado correctamente la conexion..")

