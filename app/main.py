from fastapi import FastAPI

app = FastAPI(
    title="Sistema de Gestão Empresarial",
    version="0.1.0"
)

@app.get("/")
def healt_check():
    return("status: API rodando")
