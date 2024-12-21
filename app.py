from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users
                (id INTEGER primary key AUTOINCREMENT,
                 name TEXT,
                 city TEXT,
                 rooms INTEGER,
                 price INTEGER,
                 points REAL,
                 eda TEXT,
                 stars INTEGER)
            """)

# добавляем данные в таблицу
cur.executemany("""INSERT INTO users(name, city, rooms, price, points, eda, stars)
                VALUES (?, ?, ?, ?, ?, ?, ?)""", [
                ('Санаторий “Море”', 'Сочи', 150, 12000, 9.5, 'полный пансион', 5),
                ('Санаторий “Лазурный берег”', 'Ялта', 180, 15000, 9.8, 'полный пансион', 5),
                ('Санаторий “Дагомыс”', 'Сочи', 160, 11000, 9.2, 'полупансион', 4),
                ('Санаторий “Кубань”', 'Краснодар', 140, 10000, 9, 'полный пансион', 4),
                ('Санаторий “Абрикос”', 'Анапа', 130, 9000, 8.8, 'завтраки', 4),
                ('Санаторий “Ессентуки”', 'Ессентуки', 120, 8000, 8.5, 'завтраки', 3),
                ('Санаторий “Кавказ”', 'Пятигорск', 100, 7000, 8, 'завтраки', 3),
                ('Санаторий “Ставрополь”', 'Ставрополь', 90, 6000, 7.5, 'завтраки', 3),
                ('Санаторий “Белая акватория”', 'Сочи', 80, 8500, 8.5, 'полный пансион', 4),
                ('Санаторий “Краснодар”', 'Краснодар', 70, 6500, 7.5, 'завтраки', 3)
                ]
            )
cur.execute("select * from users ")
sants= cur.fetchall()
for sant in sants:
   print(f'{sant[0]} {sant[1]} {sant[2]} {sant[3]} {sant[4]} {sant[5]} {sant[6]} {sant[7]}')
conn.commit()
conn.close()


def show_table():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()
    return render_template('table.html', rows=rows)

app = Flask(__name__)

@app.route('/')
def index():
    return show_table()

if __name__ == '__main__':
    app.run()