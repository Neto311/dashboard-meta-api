from datetime import datetime, timedelta
import random

def get_campaign_insights():
    campaign_name = "Campanha Black Friday 2025"
    ad_account_id = "act_123456789"
    
    insights = []

    for i in range(30):
        date = datetime.today() - timedelta(days=29-i)

        impressions = random.randint(5000, 20000)
        clicks = random.randint(100, 800)
        spend = round(random.uniform(100.0, 1000.0), 2)
        conversions = random.randint(10, 50)
        revenue = round(conversions * random.uniform(20.0, 100.0), 2)

        ctr = round(clicks / impressions * 100, 2)
        cpc = round(spend / clicks, 2)
        cpm = round(spend / impressions * 1000, 2)
        roas = round(revenue / spend, 2)

        insights.append({
            "date": date.strftime("%Y-%m-%d"),
            "campaign_name": campaign_name,
            "ad_account_id": ad_account_id,
            "impressions": impressions,
            "clicks": clicks,
            "spend": spend,
            "conversions": conversions,
            "revenue": revenue,
            "ctr": ctr,
            "cpc": cpc,
            "cpm": cpm,
            "roas": roas
        })

    return insights

    