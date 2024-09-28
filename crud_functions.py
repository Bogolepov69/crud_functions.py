import sqlite3

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT,
                        price INTEGER NOT NULL
                    )''')
    Products = [
        (1, 'Product1', 'Описание первого товара', 100),
        (2, 'Product2', 'Описание второго товара', 200),
        (3, 'Product3', 'Описание третьего товара', 300),
        [4, 'Product4', 'Описание четвертого товара', 400],
    ]
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Products''')
    rows = cursor.fetchall()
    conn.close()
    return rows
