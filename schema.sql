-- Deleta as tabelas se já existirem para garantir um começo limpo
DROP TABLE IF EXISTS materiais;
DROP TABLE IF EXISTS setores;

-- Tabela para armazenar os setores
CREATE TABLE setores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

-- Tabela para armazenar os materiais, com referência ao setor
CREATE TABLE materiais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    setor_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    marca TEXT,
    tombo TEXT,
    estado TEXT NOT NULL, -- (Novo, Bom, Regular)
    quantidade INTEGER DEFAULT 1,
    FOREIGN KEY (setor_id) REFERENCES setores (id)
);