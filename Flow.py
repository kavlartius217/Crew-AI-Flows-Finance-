from sentiment_analysis_crew import sentiment_crew
from investor_news import investor_news_bot
from insights_crew import insights_crew

from crewai.flow import Flow, start, listen, router, and_, or_
from pydantic import BaseModel

#State
class ExampleState(BaseModel):
  stock_name:str=" "
