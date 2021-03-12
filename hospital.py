import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='4Aepitie44!',
    database = "test"
)
mydb2 = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='4Aepitie44!',
    database = "test"

)
# print(mydb)
df =pd.read_sql_query("SELECT * FROM hospital", mydb)
# print(df)

# print(mydb2)
df2=pd.read_sql_query("SELECT * FROM doctor", mydb2)
# print(df2)

mycursor = mydb.cursor()
# mydb.commit()
# for table in mycursor:
#      print(table[2])


def get_hospital_detail(hospital_id):
    df = pd.read_sql_query("SELECT * FROM hospital WHERE like hopital_id", +str(hospital_id))
    result = mycursor.fetchall()
    print('Printing hosptal record')
    print('Hospital id', result[0][0])
    print('Hospital name',result[0],[1])
    print('Bed count', result[0],[2], '\n')
#     #Read data from Hospital table

#
def get_doctor_detail(doctor_id):
    df2 = pd.read_sql_query("SELECT * FROM doctor", + str(doctor_id))
    result = mycursor.fetchall()
    print("Printing doctor id:")
    print('Doctor ID:',result[0][0])
    print('Doctor name:', result[0],[1])
    print('Hospital ID:', result[0],[2])
    print('Joining date:', result[0],[3])
    print('Speciality:',result[0],[4])
    print('Salary:', result[0],[5])
    print("Experience:", result[0],[6],'\n')

def user_menu():
    choice = input('Please choose: \n. Get hospital detail \n2. Get doctor detail \n3. Exit\n -->')
    if choice == "1":
        hospital_id= input('Please enter hospital id \n-->')

#     # Read data from Doctor table
#
# def print_message(name, age, profession):
#         return print
# get_hospital_details(2)
# get_doctor_details(105)