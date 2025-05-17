from flask import Flask, request, render_template
import pickle
import numpy as np


app = Flask(__name__)

# Carrega o modelo salvo (ajuste o nome do arquivo se necessário)
with open("modelos/modelos.pkl", "rb") as f:
    modelos = pickle.load(f)

# Página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Rota para prever


@app.route("/prever", methods=["POST"])
def prever():
    try:
        peso = float(request.form["peso"])
        textura = float(request.form["textura"])
        docura = float(request.form["docura"])
        modelo_nome = request.form["modelo"]

        dados = np.array([[peso, textura, docura]])

        modelo_usado = modelos[modelo_nome]

        # Predição
        predicao = modelo_usado.predict(dados)[0]

        # Tentativa de pegar a confiança (probabilidade) da predição
        if hasattr(modelo_usado, "predict_proba"):
            prob = modelo_usado.predict_proba(dados)
            confianca = np.max(prob) * 100 # maior probabilidade entre classes
        else:
            # Se o modelo não suporta probabilidade (ex: SVM padrão),
            # usamos 1.0 (certeza total) ou 0.0 como fallback
            confianca = 1.0

        return render_template(
            "result.html",
            fruta=predicao,
            modelo=modelo_nome,
            confianca=confianca
        )

    except Exception as e:
        return f"<h3>Erro ao processar os dados: {str(e)}</h3><a href='/'>Voltar</a>"

if __name__ == "__main__":
    app.run(debug=True)
