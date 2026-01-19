from faker import Faker
import sqlite3
import pandas as pd

# Initialize Faker
fake = Faker(['en_US'])


def conecta_db():
    return sqlite3.connect('alumnas.db')

def crea_tabla():
    try:
        with conecta_db() as conn:
            conn.execute('''
            
            CREATE TABLE IF NOT EXISTS Students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                edad INTEGER,
                peso REAL,
                email TEXT
                );
            ''')
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    else:
        # Este bloque se ejecuta solo si el 'try' termina sin errores
        print("Tabla creada sin errores.")

# crea_tabla()

            



def inserta_datos():
    try:
        with conecta_db() as conn:
            insert_query = ('''
            
            INSERT INTO Students (nombre, edad, peso, email) 
            VALUES (?, ?, ?, ?);
            ''')
            # student_data = ('Jane Doe', 23, 51, 'jane@example.com')
            students_data = [(fake.name(), 
                              fake.random_int(min=18, max=25), 
                              fake.random_int(min=55, max=80) ,  
                              fake.email()) for _ in range(5)]

            #conn.execute(insert_query, student_data)
               # Execute the query for multiple records
            conn.executemany(insert_query, students_data)

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    else:
        # Este bloque se ejecuta solo si el 'try' termina sin errores
        print("Datos insertados sin errores.")


# inserta_datos()



''' def consulta_datos():
    try:
        with conecta_db() as conn:
            select_query = "SELECT * FROM Students;"
            
            conn.execute((select_query))

            # Fetch all records
            #all_students = cursor.fetchall()
            all_students = conn.execute(select_query).fetchall()

            # Display results in the terminal
            print("All Students:")
            for student in all_students:
                print(student)
              

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    else:
        # Este bloque se ejecuta solo si el 'try' termina sin errores
        print("Consulta sin errores.")


consulta_datos()
'''


def usa_pandas ():
    try:
        with conecta_db() as conn:
            select_query = "SELECT * FROM Students;"
            
            
    # Use pandas to read SQL query directly into a DataFrame
            df = pd.read_sql_query(select_query, conn)

    # Display the DataFrame
            print("All Students as DataFrame:")
            print(df)
              

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
    else:
        # Este bloque se ejecuta solo si el 'try' termina sin errores
        print("Consulta sin errores.")

usa_pandas()