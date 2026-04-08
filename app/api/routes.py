from fastapi import APIRouter
from app.services.db_services import salvar_insights, buscar_insights

router= APIRouter()


@router.get("/insights")
def get_insights():
    registros = buscar_insights()
    return [{
        "date": str(r.date),
        "campaign_name": r.campaign_name,
        "ad_account_id": r.ad_account_id,
        "impressions": r.impressions,
        "clicks": r.clicks,
        "spend": r.spend,
        "conversions": r.conversions,
        "revenue": r.revenue,
        "ctr": r.ctr,
        "cpc": r.cpc,
        "cpm": r.cpm,
        "roas": r.roas
        } for r in registros]


@router.get("/insights/resumo")
def get_resumo():
    registro = buscar_insights()
    total_spend = round(sum([r.spend for r in registro]), 2)
    total_revenue = round(sum([r.revenue for r in registro]), 2)
    total_conversions = round(sum([r.conversions for r in registro]))
    total_clicks = round(sum([r.clicks for r in registro]))
    total_impressions = round(sum([r.impressions for r in registro]))
    roas_medio = round(total_revenue / total_spend, 2) if total_spend else 0
    ctr_medio = round((total_clicks / total_impressions) * 100)

    resumo = {
        "total_spend": total_spend,
        "total_revenue": total_revenue,
        "total_conversions": total_conversions,
        "total_clicks": total_clicks,
        "total_impressions": total_impressions,
        "roas_medio": roas_medio,
        "ctr_medio": ctr_medio
        }
    
    return resumo