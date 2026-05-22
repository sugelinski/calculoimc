# Importa o Flask para criar o app, render_template para carregar o HTML e request para pegar os dados do formulário
from flask import Flask, render_template, request

# Inicializa a aplicação Flask
app = Flask(__name__)

# Define a rota principal da aplicação (a página inicial) que aceita requisições GET e POST
@app.route('/', methods=['GET', 'POST'])
def calcular_imc():
    # Inicializa as variáveis do resultado como None (vazias) para quando a página carregar pela primeira vez
    imc = None
    classificacao = None

    # Verifica se o usuário enviou o formulário (método POST)
    if request.method == 'POST':
        try:
            # Pega o valor do input 'peso' e converte para número decimal (float)
            peso = float(request.form['peso'])
            # Pega o valor do input 'altura' e converte para número decimal (float)
            altura = float(request.form['altura'])

            # Calcula o IMC usando a fórmula oficial: peso dividido pela altura ao quadrado
            imc = peso / (altura ** 2)
            # Arredonda o valor do IMC para duas casas decimais para ficar mais legível
            imc = round(imc, 2)

            # Estrutura condicional para definir a classificação baseada no resultado do IMC
            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif 18.5 <= imc < 24.9:
                classificacao = "Peso normal (Parabéns!)"
            elif 25 <= imc < 29.9:
                classificacao = "Sobrepeso"
            elif 30 <= imc < 34.9:
                classificacao = "Obesidade Grau 1"
            elif 35 <= imc < 39.9:
                classificacao = "Obesidade Grau 2"
            else:
                classificacao = "Obesidade Grau 3 (Mórbida)"
        
        except ValueError:
            # Caso o usuário digite algo inválido (como letras), define uma mensagem de erro
            classificacao = "Por favor, insira valores numéricos válidos."

    # Renderiza o arquivo index.html e envia as variáveis imc e classificacao para serem exibidas lá
    return render_template('index.html', imc=imc, classificacao=classificacao)

# Garante que o servidor só vai rodar se este arquivo for executado diretamente
if __name__ == '__main__':
    # Roda o aplicativo no modo de depuração (debug), que atualiza o código automaticamente ao salvar
    app.run(debug=True)