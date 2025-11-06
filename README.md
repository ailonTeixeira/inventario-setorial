# Sistema de Inventário Setorial

Sistema web para controle e inventário de patrimônio por setores, desenvolvido com Flask, Python e banco de dados SQLite. Ideal para organizações que desejam registrar, consultar e gerar relatórios dos materiais/equipamentos presentes em diferentes setores.

---

## Funcionalidades

- **Autenticação de Usuário**
  - Login obrigatório para acessar o sistema (usuário padrão: `admin`, senha padrão: `admin123`).

- **Gestão de Setores**
  - Criação automática de setores por nome.
  - Listagem dos setores existentes.
  - Interface para navegação entre setores.

- **Gestão de Materiais**
  - Cadastro, edição e remoção de materiais em cada setor.
  - Campos do material: Nome, Marca, Tombo/Patrimônio, Estado (Novo, Bom, Regular).
  - Visualização dos materiais de um setor, com destaque de estado via cores.

- **Relatórios**
  - Geração de relatório por setor em Word (.docx).
  - Geração de relatório geral em Excel (.xlsx) com todos os setores e materiais.
  - Relatório HTML por setor, com opção para imprimir/salvar em PDF.

- **Interface amigável e responsiva**
  - Utiliza Bootstrap 5 e Bootstrap Icons.
  - Navegação por menu lateral (offcanvas).
  - Mensagens de feedback para ações do usuário.

---

## Tecnologias Utilizadas

- **Backend:** Python, Flask
- **Banco de dados:** SQLite (via `database.py`)
- **Geração de relatórios:** openpyxl (Excel), python-docx (Word)
- **Frontend:** HTML, CSS, Bootstrap 5, Bootstrap Icons
- **Templates:** Jinja2 (Flask)

---

## Estrutura do Projeto

- `app.py`: arquivo principal da aplicação (rotas, lógica, geração de relatórios)
- `database.py`: camada de persistência (operações com o banco)
- `templates/`: arquivos HTML do sistema (home, login, setor, relatórios)
- `static/`: arquivos estáticos (CSS, imagens, logo)
- `inventario.db`: banco de dados SQLite (criado na inicialização)
- `schema.sql`: definições das tabelas

---

## Instalação

1. **Clone o repositório**
    ```bash
    git clone https://github.com/ailonTeixeira/inventario-setorial.git
    cd inventario-setorial
    ```

2. **Instale as dependências**
    ```bash
    pip install Flask openpyxl python-docx
    ```

3. **Inicialize o banco de dados**
    ```bash
    python
    >>> import database
    >>> database.init_db()
    >>> exit()
    ```

4. **Execute a aplicação**
    ```bash
    python app.py
    ```
    Acesse via navegador: http://localhost:5001

---

## Uso

1. Realize login com usuário e senha padrão (altere para produção).
2. Na tela inicial, digite ou selecione o nome de um setor para criar/visualizar.
3. Gerencie os materiais do setor (adicionar, editar, remover).
4. Gere relatórios em Word, Excel ou imprima PDF via interface.
5. Utilize o menu lateral para navegar pelos setores cadastrados.

---

## Personalização

- Troque o logo do sistema em `static/img/logo.png`.
- Modifique cores e estilo em `static/css/style.css`.
- Edite o usuário/senha padrão no início do arquivo `app.py`.

---

## Licença

Este projeto é open-source sob a Licença MIT.

---

## Autor

- Ailon Teixeira
- [github.com/ailonTeixeira](https://github.com/ailonTeixeira)
