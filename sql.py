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


def fetch_attendance():
    global cursor

    cursor.execute(f"select id,name,grade from users where role = 'member' and active = true order by rollno")

    results = cursor.fetchall()

    result1 = {9: [],
               10:[],
               11:[],
               12:[]}
    for result in results:
        result1[result[2]].append({"id":result[0],"name":result[1]})
    
    return result1

def fetch_roletakers():
    global cursor

    cursor.execute(f"select id,name,grade,role from users where active = true order by rollno")

    results = cursor.fetchall()

    result1 = {'9': [],
                '10':[],
                '11':[],
                '12':[]}
    results2 = []
    
    for result in results:
        match result[3]:
            case 'officer' | 'oc':
                results2.append({"id":result[0],"name":result[1]})
                

            case 'member':
                result1[str(result[2])].append({"id":result[0],"name":result[1]})
    
    for grade in result1.values():
        grade.extend(results2)
    
    print(results2)

    return result1
