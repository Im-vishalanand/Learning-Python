from flask import Flask, request, jsonify
import sqlite3


app = Flask(__name__)


conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

conn.commit()
conn.close()


@app.route('/records', methods=['POST'])
def create_record():
    name = request.json['name']
    email = request.json['email']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('INSERT INTO records (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Record created successfully'})


@app.route('/records', methods=['GET'])
def get_records():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('SELECT * FROM records')
    records = c.fetchall()

    conn.close()

    return jsonify(records)


@app.route('/records/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    name = request.json['name']
    email = request.json['email']

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('UPDATE records SET name = ?, email = ? WHERE id = ?', (name, email, record_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Record updated successfully'})


@app.route('/records/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('DELETE FROM records WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Record deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
