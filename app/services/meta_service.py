import os
import dotenv
import requests

def get_facebook_ads_data():
    dotenv.load_dotenv()
    access_token = os.getenv("META_ACCESS_TOKEN")
    ad_account_id = os.getenv("META_AD_ACCOUNT_ID")
    api_version = os.getenv("META_API_VERSION")

    url = f"https://graph.facebook.com/{api_version}/{ad_account_id}/insights"
    params = {
        "access_token": access_token,
        "fields": "campaign_name,impressions,clicks,spend, actions, action_values",
        "date_preset": "last_30d",
        "time_increment": "1",
        "level": "campaign"}

    data = requests.get(url, params=params).json()

    if 'error' in data:
        print(f"Erro ao obter dados do Facebook Ads: {data['error']['message']}")
        return []
    else:
        return data.get("data", [])
    

def formatar_insights(raw_insights):
    insights_formatados = []
    for item in raw_insights:
        clicks = int(item.get('clicks', 0)) if raw_insights else 0
        impressions = int(item.get('impressions', 0)) if raw_insights else 0
        spend = float(item.get('spend', 0)) if raw_insights else 0
        insights_formatados.append({
            'date': item.get('date_start'),
            'campaign_name': item.get('campaign_name'),
            'ad_account_id': os.getenv("META_AD_ACCOUNT_ID"),
            'impressions': int(item.get('impressions', 0)),
            'clicks': int(item.get('clicks', 0)),
            'spend': float(item.get('spend', 0)),
            'conversions': int(next((action['value'] for action in item.get('actions', []) if action['action_type'] == 'purchase'), 0)),
            'revenue': float(next((action_value['value'] for action_value in item.get('action_values', []) if action_value['action_type'] == 'purchase'), 0)),
            'ctr': clicks / impressions if impressions > 0 else 0,
            'cpc': spend / clicks if clicks > 0 else 0,
            'cpm': (spend / impressions) * 1000 if impressions > 0 else 0,
            'roas': (float(next((action_value['value'] for action_value in item.get('action_values', []) if action_value['action_type'] == 'purchase'), 0)) / spend) if spend > 0 else 0
        })
    return insights_formatados







    