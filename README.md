
```markdown
# Classificação de Frutas com Modelos de Machine Learning

Este projeto apresenta um pipeline completo para classificação de frutas usando modelos de Machine Learning em Python.  
Ele inclui:

- Geração de um dataset fictício e já tratado (peso, textura, docura, etc)  
- Treinamento de 3 modelos: KNN, Random Forest e SVM  
- Avaliação de desempenho dos modelos  
- Backend em Flask para realizar previsões interativas via formulário web  
- Visualização dos resultados e confiança da predição

---

## Tecnologias

- Python 3.x  
- scikit-learn  
- Flask  
- matplotlib / seaborn  
- Jupyter Notebook  

---

## Estrutura do repositório

```

/
├── app.py                 # Código backend Flask
├── modelos.pkl            # Modelos treinados serializados
├── notebook.ipynb         # Notebook com todo o pipeline de ML
├── templates/             # Templates HTML para a aplicação Flask
│   ├── index.html
│   └── result.html
├── static/                # Arquivos estáticos (CSS, JS)
│   └── style.css
└── README.md              # Este arquivo

````

---

## Como usar

### 1. Clonar o repositório

```bash
git clone https://github.com/karython/seu-repositorio.git
cd seu-repositorio
````

### 2. Instalar dependências

Recomenda-se usar um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

> *Se ainda não houver um `requirements.txt`, crie-o com:*

```bash
pip freeze > requirements.txt
```

### 3. Rodar o notebook

Abra o `notebook.ipynb` no Jupyter para explorar a criação do dataset, o treinamento dos modelos e as análises.

### 4. Rodar o backend Flask

```bash
python app.py
```

Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

Preencha o formulário, escolha o modelo e veja a previsão com a confiança em porcentagem.

---

## Contato

Se tiver dúvidas ou sugestões, entre em contato:
📧 [karython.unai@gmail.com](mailto:karython.unai@gmail.com)
🐙 GitHub: [@karython](https://github.com/karython)

---

## Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

