import psycopg2

database = psycopg2.connect(
    host='10.1.1.53',
    user='techmail',
    password='tech2020',
    database='techmail'
)

cursor = database.cursor()

