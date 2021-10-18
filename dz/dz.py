import sqlite3
import random

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def print_question(connection, level):
    rnd_id = str(random.choice([1,2]))
    print(execute_read_query(connection, "SELECT Question FROM level" + level + " WHERE id="+rnd_id+";")[0][0])
    print('Варианты ответов:')
    for i in range(1,5):
        print(execute_read_query(connection, "SELECT V"+str(i)+" FROM level" + level + " WHERE id="+rnd_id+";")[0][0])
    answer = int(input())
    right_answer = execute_read_query(connection, "SELECT Answer FROM level" + level + " WHERE id="+rnd_id+";")[0][0]
    if (answer == right_answer):
        print('Это верный ответ')
    else:
        print('Вы ответили не верно')
        raise SystemExit

con = sqlite3.connect("Quiz")
for i in range(1,6):
    print_question(con, str(i))
print('Ты молоец')
con.close()