# 🏆 Simulador de Copa do Mundo 2026

![Demonstração do algoritmo](https://github.com/user-attachments/assets/218f43e3-982d-475d-bb6f-40476986d0a0)

Projeto desenvolvido em Python para simular as fases eliminatórias da Copa do Mundo de 2026, com geração automática de resultados, disputa de pênaltis em caso de empate e armazenamento dos dados em banco SQLite.

## 🚀 Tecnologias Utilizadas

- Python 3
- SQLite
- SQL

## ⚙️ Funcionalidades

- Simulação das oitavas de final
- Simulação das quartas de final
- Simulação das semifinais
- Simulação da final
- Geração aleatória de placares
- Decisão por pênaltis em partidas empatadas
- Armazenamento dos resultados em banco de dados SQLite
- Consultas SQL para análise dos dados gerados

## 📂 Estrutura do Projeto

```text
Simulador-de-Copa-2026/
│
├── copa.py
├── consultas.sql
├── copa2026.db
├── requirements.txt
└── README.md
```

## ▶️ Como Executar

1. Certifique-se de possuir o Python 3 instalado.
2. Clone o repositório:

```bash
git clone https://github.com/HerbertsDev/Simulador-de-Copa-2026.git
```

3. Acesse a pasta do projeto:

```bash
cd Simulador-de-Copa-2026
```

4. Execute o programa:

```bash
python copa.py
```

## 📊 Exemplo de Saída

```text
Oitavas de Final
Brasil 2 x 1 México → Classificado: Brasil

Quartas de Final
Brasil 1 x 0 Argentina → Classificado: Brasil

🏆 Campeão da Copa 2026: Brasil
```

## 🗄️ Banco de Dados

Todos os resultados das partidas são armazenados em um banco SQLite, permitindo consultas e análises posteriores por meio dos scripts disponíveis em `consultas.sql`.

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de praticar:

- Lógica de programação
- Estruturas de controle
- Manipulação de banco de dados
- Consultas SQL
- Organização de projetos em Python

## 👨‍💻 Autor

Herbert Da Silva Da Cruz

Projeto desenvolvido para fins de estudo e aprimoramento das habilidades em Python e Banco de Dados.
