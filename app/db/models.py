from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class CampaignInsight(Base):
    __tablename__ = 'campaign_insights'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    campaign_name = Column(String, nullable=False)
    ad_account_id = Column(String, nullable=False)
    impressions = Column(Integer)
    clicks = Column(Integer)
    spend = Column(Float)
    conversions = Column(Integer)
    revenue = Column(Float)
    ctr = Column(Float)
    cpc = Column(Float)
    cpm = Column(Float)
    roas = Column(Float)

    def __repr__(self):
        return f"<CampaingInsights {self.date} | {self.campaign_name}>"
    