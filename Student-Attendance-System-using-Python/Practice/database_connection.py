import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'attendance_system',
  'raise_on_warnings': True
}

mydba = mysql.connector.connect(**config)
mycursor = mydba.cursor()


def query_fire(query):
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result


if __name__ == '__main__':
    print('Welcome to the SQL query fire python program...!')
    while True:
        query = input('Enter your query: ')
        try:
            print(query_fire(query))
            mydba.commit()
        except mysql.connector.Error as Error:
            print('Error Occured: ', Error.msg)
            mydba.rollback()
            exit()
        else:
            print('Query run succesfully...!')
        continue