import psycopg2

params = {
    'user' : 'darthkitten2228',
    'password': 'Bi4E8vlSCodf',
    'database': '2023-2024',
    'host': 'ep-twilight-mud-18405172.ap-southeast-1.aws.neon.tech' 
}

conn = psycopg2.connect(**params)
cursor = conn.cursor()

def new_meeting(meetingid,date):
    global cursor

    cursor.execute(f"insert into meetings(id,date) values({meetingid},{date})")
    cursor.execute("commit")


def add_sheet(meetingid,type,sheet):
    global cursor

    meeting_sheet = type+'_sheet'
    cursor.execute(f"update meetings set {meeting_sheet} = {sheet} where id = {meetingid}")
    cursor.execute("commit")


def fetch_attendance(grade):
    global cursor

    cursor.execute(f"select id,name from users where role = 'member' and grade = {grade} and active = true order by rollno")

    results = cursor.fetchall()
    
    return results