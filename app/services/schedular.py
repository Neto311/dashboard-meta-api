from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from app.services.db_services import buscar_insights
from app.services.report_service import gerar_pdf

def gerar_relatorio_semanal():
    print(f"Gerando relatório semanal ...")
    data_inicio = datetime.now().date() - timedelta(days=7)
    data_final = datetime.now().date()
    registros = buscar_insights(data_inicio, data_final)
    if registros:
        dados = [r.__dict__ for r in registros]
        gerar_pdf(dados)
        print("Relatório semanal gerado com sucesso!")
    else:
        print("Nenhum dado para gerar relatório semanal.")


def gerar_relatorio_mensal():
    print(f"Gerando relatório mensal ...")
    data_inicio = datetime.now().date() - timedelta(days=30)
    data_final = datetime.now().date()
    registros = buscar_insights(data_inicio, data_final)
    if registros:
        dados = [r.__dict__ for r in registros]
        gerar_pdf(dados)
        print("Relatório mensal gerado com sucesso!")
    else:
        print("Nenhum dado para gerar relatório mensal.")

def iniciar_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(gerar_relatorio_semanal, 'cron', day_of_week='sat', hour=8, minute=0)
    scheduler.add_job(gerar_relatorio_mensal, 'cron', day_of_week='sat', hour=8, minute=0)
    scheduler.start()
    print("Scheduler iniciado para geração de relatórios semanais e mensais.")
    return scheduler
