import json
import re

class ProcessadorTexto:
    def __init__(self, arquivo_expressoes):
        self.expressoes = self.carregar_expressoes(arquivo_expressoes)
    
    def carregar_expressoes(self, arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return [linha.strip().lower() for linha in f.readlines() if linha.strip()]

    @staticmethod
    def dividir_sentencas(texto):
        return re.split(r"(?<=[.!?])\s+", texto)

    @staticmethod
    def tokenizar(texto):
        return re.findall(r"\w+|[^\w\s]", texto, re.UNICODE)

    def encontrar_expressao(self, sentenca):
        tokens_sentenca = [token.lower() for token in self.tokenizar(sentenca)]
        
        for expressao in self.expressoes:
            tokens_expressao = self.tokenizar(expressao)
            tokens_expressao = [token.lower() for token in tokens_expressao]
            exp_len = len(tokens_expressao)
            
            for i in range(min(3, len(tokens_sentenca) - exp_len + 1)):
                if tokens_sentenca[i:i+exp_len] == tokens_expressao:
                    return expressao
        return None

class ProcessadorArquivo:
    def __init__(self, arquivo_entrada, arquivo_saida, arquivo_expressoes):
        self.arquivo_entrada = arquivo_entrada
        self.arquivo_saida = arquivo_saida
        self.processador_texto = ProcessadorTexto(arquivo_expressoes)

    def processar(self):
        with open(self.arquivo_entrada, "r", encoding="utf-8") as f:
            textos = json.load(f)

        resultado = []
        
        for item in textos:
            id_texto = item["id"]
            sentencas = self.processador_texto.dividir_sentencas(item["texto"])
            
            resultado_texto = {
                "id": id_texto,
                "sentencas": []
            }

            for sentenca in sentencas:
                expressao = self.processador_texto.encontrar_expressao(sentenca)
                resultado_texto["sentencas"].append({
                    "sentenca": sentenca,
                    "expressao": expressao if expressao else None
                })

            resultado.append(resultado_texto)
        
        with open(self.arquivo_saida, "w", encoding="utf-8") as f:
            json.dump(resultado, f, ensure_ascii=False, indent=2)
