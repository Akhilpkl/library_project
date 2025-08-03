from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

def get_connection():
    return pymysql.connect(host='localhost', user='root', password='akhilpkl@123', database='library_db')
@app.route('/')
def home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    conn.close()
    return render_template("home.html", books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_book.html')


@app.route('/members')
def view_members():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")
    members = cur.fetchall()
    conn.close()
    return render_template("members.html", members=members)

@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO members (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        conn.close()
        return redirect('/members')
    return render_template("add_member.html")

@app.route('/search')
def search():
    query = request.args.get('query', '').strip()

    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
        like_query = f"%{query}%"
        cursor.execute(sql, (like_query, like_query))
        results = cursor.fetchall()
    connection.close()

    return render_template('search_results.html', books=results, query=query)
@app.route('/all_books')
def view_allbooks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    conn.close()
    return render_template("all_books.html", books=books)

<<<<<<< HEAD
@app.route('/about')
def abouts():
    return render_template("about.html")

=======
>>>>>>> 1460bead0e7b6f19a69737e63efbda398a54e8fc
if __name__ == '__main__':
    app.run( debug=True)
