from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
import shutil
import os
import json
from typing import List
from text_processor import ProcessadorArquivo
from rule_processor import RuleProcessor

router = APIRouter()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
EXPRESSOES_FILE = "amostras/expressoes.txt"
REGRAS_FILE = "regras/regras_linguagem_natural.txt"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def validar_estrutura_json(textos: List[dict]):
    for item in textos:
        if "id" not in item or "texto" not in item:
            return False
    return True

def processar_background(file_path: str, output_path: str):
    processador = ProcessadorArquivo(file_path, output_path, EXPRESSOES_FILE)
    processador.processar()

    with open(file_path, "r", encoding="utf-8") as f:
        textos = json.load(f)
    
    rule_processor = RuleProcessor(REGRAS_FILE, EXPRESSOES_FILE)
    resultado = rule_processor.aplica_regras(textos)

    output_path_rules = os.path.join(OUTPUT_DIR, "saida_p2.json")
    with open(output_path_rules, "w", encoding="utf-8") as f:
        json.dump(resultado, f, ensure_ascii=False, indent=2)
    
    os.remove(file_path)

@router.post("/processar", response_model=dict, description="Processa um arquivo JSON de entrada e executa duas etapas de processamento.", status_code=202)
async def processar_arquivo(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="Arquivo para o processamento nao foi informado.")

    if not file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="arquivo inválido")
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            textos = json.load(f)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Arquivo JSON mal formado")
    
    if not validar_estrutura_json(textos):
        raise HTTPException(status_code=400, detail="o formato correto exige as seguintes chaves id e texto")
    
    output_path = os.path.join(OUTPUT_DIR, "saida_p1.json")
    
    background_tasks.add_task(processar_background, file_path, output_path)
    
    return JSONResponse(content={"status": "Processamento iniciado com sucesso, aguarde..."}, status_code=202)
