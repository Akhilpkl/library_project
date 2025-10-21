from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database connection function
def get_connection():
    return pymysql.connect(host='localhost', user='root', password='akhilpkl@123', database='library_db')

# ------------------ HOME PAGE ------------------
@app.route('/')
def home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    conn.close()
    return render_template("home.html", books=books)

# ------------------ ADD BOOK ------------------
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

# ------------------ UPDATE BOOK ------------------
@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        cur.execute("UPDATE books SET title=%s, author=%s WHERE id=%s", (title, author, book_id))
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        cur.execute("SELECT * FROM books WHERE id=%s", (book_id,))
        book = cur.fetchone()
        conn.close()
        return render_template("edit_book.html", book=book)

# ------------------ DELETE BOOK ------------------
@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=%s", (book_id,))
    conn.commit()
    conn.close()
    return redirect('/')

# ------------------ VIEW MEMBERS ------------------
@app.route('/members')
def view_members():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")
    members = cur.fetchall()
    conn.close()
    return render_template("members.html", members=members)

# ------------------ ADD MEMBER ------------------
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

# ------------------ UPDATE MEMBER ------------------
@app.route('/edit_member/<int:member_id>', methods=['GET', 'POST'])
def edit_member(member_id):
    conn = get_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur.execute("UPDATE members SET name=%s, email=%s WHERE id=%s", (name, email, member_id))
        conn.commit()
        conn.close()
        return redirect('/members')
    else:
        cur.execute("SELECT * FROM members WHERE id=%s", (member_id,))
        member = cur.fetchone()
        conn.close()
        return render_template("edit_member.html", member=member)

# ------------------ DELETE MEMBER ------------------
@app.route('/delete_member/<int:member_id>')
def delete_member(member_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM members WHERE id=%s", (member_id,))
    conn.commit()
    conn.close()
    return redirect('/members')

# ------------------ SEARCH ------------------
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

# ------------------ ALL BOOKS ------------------
@app.route('/all_books')
def view_allbooks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    conn.close()
    return render_template("all_books.html", books=books)

# ------------------ ABOUT ------------------
@app.route('/about')
def abouts():
    return render_template("about.html")

# ------------------ MAIN ------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
