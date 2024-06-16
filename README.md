# Modelo Estatístico para prever o resultado de uma partida de League of Legends

Olá, meu nome é Shady! Prazer, este é o meu TCC do curso de Ciência de Dados da EBAC. Além de um TCC, esse projeto também faz parte do programa de parceria com a Semantix, com a possibilidade de contratação pela Empresa.

Primeiramente eu gostaria de fazer uma breve apresentação. Tenho 20 anos, comecei a programar aos 14 quando aprendi minha primeira linguagem de programação(Python). Meu interesse por programação veio graças à minha paixão por jogos, pois sempre sonhei em fazer um jogo, sonho que eu mantenho até os dias de hoje. Desenvolvi diversos projetos pessoais, seja em Python ou outras linguagens. Mais pra frente, aos 19 anos, comecei a me interessas pela área de dados devido ao seu constante crescimento e interesse em modelos de inteligência artificial.


# Construção do projeto:

A construção do projeto consiste em 5 etapas:

- Mineração dos dados na API da riot
- Limpeza e transformação dos dados
- Construção do Modelo
- Análise exploratória
- Criação de uma interface usando Streamlit


Você pode acompanhar cada etapa na pasta ``/notebooks`` desde projeto, na ordem mostrada acima.

# Interface

Na nossa última etapa, criamos uma interface utilizando Streamlit que irá consultar todas as suas últimas 10 partidas de Lol e o modelo irá calcular a probabilida de vitória dessas partidas, além de comparar o resultado real da partida com o predito. Você pode acessar a interface através desse link: https://predict-lol-match.streamlit.app/

#### E para finalizar, dizer muito obrigado à EBAC pelo excelente curso, e dizer à Semantix que eu ficaria extremamente honrado em trabalhar pra empresa 😊😊😊😊

- Linkedin: https://www.linkedin.com/in/shadyrajaab/
- Github: https://github.com/shadyrajab
- E-mail: shadyrajaab@gmail.com
- Telefone: 61 99820-7214

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [pandas](https://pandas.pydata.org/)
- [imbalanced-learn (SMOTE)](https://imbalanced-learn.org/stable/)
- [requests](https://pypi.org/project/requests/)


# API da riot

Você pode criar um token da API da Riot através desse link: https://developer.riotgames.com/

## Como Executar o Projeto

### Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório para sua máquina local:

```sh
git clone https://github.com/shadyrajab/predict-lol-match
```

2. Crie um ambiente virtual:
```sh
python -m venv venv
```
3. Instale as dependências:
```sh
pip install -r requirements.txt
```

# Executando a Aplicação
```sh
streamlit run Início.py
```

[streamlit-Início-2024-06-16-17-06-87.webm](https://github.com/shadyrajab/predict-lol-match/assets/65933264/70dd2a20-b2e7-4287-bf6a-8ec8ef21bcb9)


