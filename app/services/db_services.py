from datetime import datetime, timedelta   
from app.db.database import get_session
from app.db.models import CampaignInsight

def salvar_insights(insights: list):
    session = get_session()

    try:
        salvos = 0
        for item in insights:
            registro = CampaignInsight(
                date=datetime.strptime(item["date"], "%Y-%m-%d").date(),
                campaign_name=item["campaign_name"],
                ad_account_id=item["ad_account_id"],
                impressions=item["impressions"],
                clicks=item["clicks"],
                spend=item["spend"],
                conversions=item["conversions"],
                revenue=item["revenue"],
                ctr=item["ctr"],
                cpc=item["cpc"],
                cpm=item["cpm"],
                roas=item["roas"]
            )
            session.add(registro)
            salvos += 1 
            
        session.commit()
        print(f"{salvos} registros salvos com sucesso!")

    except Exception as e:
        session.rollback()
        print(f"Erro ao salvar insights: {e}")
    
    finally:
        session.close()


def buscar_insights(data_inicio, data_final):
    session = get_session()
    try:
        registros = session.query(CampaignInsight).order_by(CampaignInsight.date).filter(CampaignInsight.date >= data_inicio, CampaignInsight.date <= data_final).all()
        return registros
    finally:
        session.close()