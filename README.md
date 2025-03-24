# 📌 Módulo de Processamento de Regras

Este repositório contém um módulo Python projetado para processar regras e expressões em sentenças, utilizando um sistema baseado em arquivos de regras e expressões.

## 🚀 Tecnologias Utilizadas

- **Python 3.9+**
- **FastAPI**
- **Pytest** Não foi implementado testes automatizados devido ao tempo esgotado
- **Docker** para conteinerização
- **Filas de processamento** No processamento dos textos são enviados os arquivos para uma fila 

## 📂 Estrutura do Projeto

```
.
├── amostras
│   └── expressoes.txt
├── api.py
├── docker-compose.yml
├── Dockerfile
├── outputs
│   ├── saida_p1.json
│   └── saida_p2.json
├── PROBLEMA.md
├── README.md
├── regras
│   └── regras_linguagem_natural.txt
├── requirements.txt
├── routers
│   ├── exibir_saida_p1.py
│   ├── exibir_saida_p2.py
│   ├── processar_arquivo.py
│   └── verificar_status.py
├── rule_processor.py
├── text_processor.py
└── uploads
```

## 🛠️ Instalação e Uso

### 🔧 Clonando o Repositório
```bash
git git remote add origin https://github.com/lmtharlleste/alleasy_desafio.git
cd alleasy_desafio
```

### ⚙️ Configuração com Docker
```bash
docker-compose up --build -d  // retire o -d pra verificar os logs do sistema)
```

## 📖 Endpoints da API

| Método | Endpoint     | Descrição                         |
|---------|-------------|---------------------------------|
| POST     | `/processar`| Realizando processamento dos arquivos passando o arquivo json com a chave file |
| GET    | `/verificar`  | Verificar se o processamento foi finalizado |
| GET    | `/exibir_saida_p1`  | Realizar leitura do arquivo de processamento |
| GET    | `/exibir_saida_p2`  | Realizar leitura do arquivo de regras|

## Formato de Requisição para /processar
O endpoint /processar espera uma requisição com form_data, sendo necessário enviar um arquivo JSON com o seguinte formato:

```bash
{
  "file": "nome_do_arquivo_aqui.json"
}
```

## 📜 OBSERVAÇÃO
Foram encontradas discrepâncias no arquivo de amostra das regras, cujo a saída esperada é:

```bash
[
  {
    "id": 1,
    "categorias": [
      "A",
      "B"
    ]
  },
  {
    "id": 4,
    "categorias": [
      "C"
    ]
  }
]

```
Mas, pela lógica proposta no arquivo de regras e descritas como foi encontrada o problema no arquivi PROBLEMA.md, a saída gerada está assim:
```bash
[
  {
    "id": 1,
    "categorias": [
      "A",
      "B"
    ]
  },
  {
    "id": 4,
    "categorias": [
      "D"
    ]
  }
]
```
Peço descuçpas se faltou algo! Deus seja louvado por tudo!!