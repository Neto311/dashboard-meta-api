from app.db.database import init_db
from app.services.meta_service import get_campaign_insights
from app.services.db_services import salvar_insights, buscar_insights
from app.api.routes import router
from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(router, prefix="/api")

@app.on_event("startup")
def startup_event():
    init_db()
    dados = get_campaign_insights()
    salvar_insights(dados)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


