from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import os
import json

router = APIRouter()

OUTPUT_DIR = "outputs"

@router.get("/exibir_saida_p2", response_model=dict, description="Exibe o conteúdo do arquivo de saída `saida_p2.json`.", status_code=200)
async def exibir_saida_p2():
    output_path_p2 = os.path.join(OUTPUT_DIR, "saida_p2.json")
    
    if os.path.exists(output_path_p2):
        with open(output_path_p2, "r", encoding="utf-8") as file:
            conteudo = json.load(file)
        return JSONResponse(content={"status": "Conteúdo do arquivo saida_p2.json", "conteudo": conteudo}, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Arquivo saida_p2.json não encontrado")
