import psycopg2

params = {
    'user' : 'darthkitten2228',
    'password': 'Bi4E8vlSCodf',
    'database': '2023-2024',
    'host': 'ep-twilight-mud-18405172.ap-southeast-1.aws.neon.tech' 
}

conn = psycopg2.connect(**params)
cursor = conn.cursor()

