#from django.shortcuts import render
from django.http import HttpResponse
import sqlite3

# Create your views here.
def books(request):
    with sqlite3.connect("firstdb.sqlite3") as conn:
        cur = conn.cursor()

        qryAddRecords = '''
            INSERT INTO Books ('id', 'name', 'email') VALUES
                ('1', 'Robert', 'rob@gmail.com'),
                ('2', 'Mike', 'mike@gmail.com'),
                ('3', 'Sarah', 'sarah@gmail.com')
        '''
        cur.execute(qryAddRecords)

        qryFetchAllRecords = "SELECT * FROM Books"

        cur.execute(qryFetchAllRecords)

        books=cur.fetchall()

        conn.commit()

    return HttpResponse(str(books))

def book(request, id):
    with sqlite3.connect("firstdb.sqlite3") as conn:
        cur = conn.cursor()

        cur.execute("SELECT * FROM Books WHERE id=(?)", (id,))

        book=cur.fetchone()

    return HttpResponse(str(book))
