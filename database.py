import sqlite3

DATABASE_NAME = 'inventario.db'

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = get_db()
    with open('schema.sql', 'r') as f:
        db.executescript(f.read())
    db.commit()

# --- Funções para Setores ---
def get_todos_setores():
    db = get_db()
    setores = db.execute('SELECT * FROM setores ORDER BY nome').fetchall()
    db.close()
    return setores

def get_setor_por_nome(nome):
    db = get_db()
    setor = db.execute('SELECT * FROM setores WHERE nome = ?', (nome,)).fetchone()
    db.close()
    return setor

def get_setor_por_id(setor_id):
    db = get_db()
    setor = db.execute('SELECT * FROM setores WHERE id = ?', (setor_id,)).fetchone()
    db.close()
    return setor

def adicionar_setor(nome):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO setores (nome) VALUES (?)', (nome,))
    new_id = cursor.lastrowid
    db.commit()
    db.close()
    return new_id

# --- Funções para Materiais ---
def get_materiais_por_setor(setor_id):
    db = get_db()
    materiais = db.execute(
        'SELECT * FROM materiais WHERE setor_id = ? ORDER BY nome', (setor_id,)
    ).fetchall()
    db.close()
    return materiais

def adicionar_material(dados):
    db = get_db()
    db.execute(
        'INSERT INTO materiais (setor_id, nome, marca, tombo, estado) VALUES (?, ?, ?, ?, ?)',
        (dados['setor_id'], dados['nome'], dados['marca'], dados['tombo'], dados['estado'])
    )
    db.commit()
    db.close()

def atualizar_material(material_id, dados):
    db = get_db()
    db.execute(
        'UPDATE materiais SET nome = ?, marca = ?, tombo = ?, estado = ? WHERE id = ?',
        (dados['nome'], dados['marca'], dados['tombo'], dados['estado'], material_id)
    )
    db.commit()
    db.close()

def apagar_material(material_id):
    db = get_db()
    db.execute('DELETE FROM materiais WHERE id = ?', (material_id,))
    db.commit()
    db.close()