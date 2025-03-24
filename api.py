from fastapi import FastAPI
from routers import processar_arquivo, verificar_status, exibir_saida_p1, exibir_saida_p2

app = FastAPI()

app.include_router(processar_arquivo.router)
app.include_router(verificar_status.router)
app.include_router(exibir_saida_p1.router)
app.include_router(exibir_saida_p2.router)
