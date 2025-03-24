from fastapi import APIRouter
from fastapi.responses import JSONResponse
import os

router = APIRouter()

OUTPUT_DIR = "outputs"

@router.get("/verificar", response_model=dict, description="Verifica o status do processamento dos arquivos.", status_code=200)
async def verificar_status():
    output_path_p1 = os.path.join(OUTPUT_DIR, "saida_p1.json")
    output_path_p2 = os.path.join(OUTPUT_DIR, "saida_p2.json")

    if os.path.exists(output_path_p1) and os.path.exists(output_path_p2):
        return JSONResponse(content={"status": "Processamento concluído", "files": [output_path_p1, output_path_p2]}, status_code=200)
    else:
        return JSONResponse(content={"status": "Processamento não iniciado ou não finalizado!"}, status_code=202)
