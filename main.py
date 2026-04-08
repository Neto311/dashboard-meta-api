from app.db.database import init_db
from app.services.meta_service import get_facebook_ads_data, formatar_insights
from app.services.db_services import salvar_insights, buscar_insights
from app.api.routes import router
from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(router, prefix="/api")

@app.on_event("startup")
def startup_event():
    init_db()
    dados = formatar_insights(get_facebook_ads_data())
    salvar_insights(dados)
    print(f"Dados recebidos: {len(dados)} insights formatados e salvos no banco de dados.")
    print(dados[0] if dados else "Nenhum dado recebido.")
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


