# credit-rating-api

### Iniciar a aplicação

1. Crie o ambiente virtual:

```bash
python3 -m venv venv
```

2. Ative o ambiente virtual:

```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

(No Windows use )

3. Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

4. Rode o servidor

```bash
python3 app.py
```

### Estrutura do Projeto

```bash
credit-rating-api/
├── models/
│   └── pipeline_logistica.pkl
│
├── routes/
│   └── route.py
│
├── schemas/
│   ├── __init__.py
│   └── form_schema.py
│
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```
