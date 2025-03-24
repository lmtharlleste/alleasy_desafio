import json
import re
from text_processor import ProcessadorTexto

NUM_WORDS = {
    "um": 1, "uma": 1,
    "dois": 2, "duas": 2,
    "três": 3, "quatro": 4,
    "cinco": 5, "seis": 6,
    "sete": 7, "oito": 8,
    "nove": 9, "dez": 10
}

def extrair_valor(condicao_str):
    match = re.search(r'\d+', condicao_str)
    if match:
        return int(match.group())
    else:
        for palavra, valor in NUM_WORDS.items():
            if palavra in condicao_str:
                return valor
    return None

def parse_operator(condicao_str):
    if "maior ou igual a" in condicao_str:
        return lambda a, b: a >= b
    elif "menor ou igual a" in condicao_str:
        return lambda a, b: a <= b
    elif "mais de" in condicao_str or "maior que" in condicao_str:
        return lambda a, b: a > b
    elif "menor que" in condicao_str:
        return lambda a, b: a < b
    elif "igual a" in condicao_str:
        return lambda a, b: a == b
    else:
        return None

def parse_condition(cond_str):
    cond = cond_str.strip().lower()
    if "número de sentenças com expressões" in cond:
        attr = "num_sentences_with_expressions"
        op = parse_operator(cond)
        valor = extrair_valor(cond)
        return lambda metrics: op(metrics[attr], valor)
    elif "número de sentenças" in cond:
        attr = "num_sentences"
        op = parse_operator(cond)
        valor = extrair_valor(cond)
        return lambda metrics: op(metrics[attr], valor)
    elif "número de tokens" in cond:
        attr = "num_tokens"
        op = parse_operator(cond)
        valor = extrair_valor(cond)
        return lambda metrics: op(metrics[attr], valor)
    elif "presença de token" in cond:
        match = re.search(r'\"(.+?)\"', cond)
        if match:
            token_proc = match.group(1).lower()
            return lambda metrics: token_proc in metrics["tokens"]
        else:
            return lambda metrics: False
    elif "presença de expressões" in cond:
        return lambda metrics: metrics["has_expressions"]
    return lambda metrics: False

class RuleProcessor:
    def __init__(self, arquivo_regras, arquivo_expressoes):
        self.arquivo_regras = arquivo_regras
        self.regras = self._carregar_regras()
        self.processador_texto = ProcessadorTexto(arquivo_expressoes)
    
    def _carregar_regras(self):
        regras = []
        with open(self.arquivo_regras, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                try:
                    cond_part, categ_part = linha.split(", então a categoria é")
                except ValueError:
                    continue
                cond_part = cond_part.replace("Se", "", 1).strip()
                condicoes_str = [c.strip() for c in cond_part.split(" e ")]
                condicoes_funcoes = [parse_condition(cond) for cond in condicoes_str]
                categoria = categ_part.strip().rstrip('.')
                regras.append({
                    "conditions": condicoes_funcoes,
                    "categoria": categoria
                })
        return regras

    def _calcular_metricas(self, texto):
        sentencas = self.processador_texto.dividir_sentencas(texto)
        num_sentences = len(sentencas)
        tokens = self.processador_texto.tokenizar(texto)
        tokens = [token.lower() for token in tokens]
        num_tokens = len(tokens)
        
        has_expressions = False
        num_sentences_with_expressions = 0
        for sent in sentencas:
            exp = self.processador_texto.encontrar_expressao(sent)
            if exp:
                has_expressions = True
                num_sentences_with_expressions += 1
        
        num_commas = texto.count(',')
        
        return {
            "num_sentences": num_sentences,
            "num_tokens": num_tokens,
            "tokens": set(tokens),
            "has_expressions": has_expressions,
            "num_sentences_with_expressions": num_sentences_with_expressions,
            "num_commas": num_commas
        }

    def aplica_regras(self, lista_textos):
        resultados = []
        for item in lista_textos:
            texto = item["texto"]
            id_texto = item["id"]
            metrics = self._calcular_metricas(texto)
            categorias = set()
            
            for regra in self.regras:
                if all(cond(metrics) for cond in regra["conditions"]):
                    categorias.add(regra["categoria"])
            
            resultados.append({
                "id": id_texto,
                "categorias": sorted(categorias)
            })
        
        return resultados
