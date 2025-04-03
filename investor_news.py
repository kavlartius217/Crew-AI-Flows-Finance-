from crewai import Agent, Task, Crew 
from crewai.project import agent, task, crew, CrewBase
from crewai_tools import SerperDevTool

web_search_tool=SerperDevTool()


@CrewBase
class investor_news_bot():
  def news_agent(self)->Agent:
    return Agent(
      role="positve_news_agent",
      goal="Based on the stock name find positive news about the stock encouraging the investor to invest in that particular stock",
      backstory="You are an expert in encouraging investors in buying stock which have a positive public sentiment based on the current stock news",
      tools=[web_search_tool]
    )
  
  @task
  def news_task(self)->Task:
    return Task(
      description="Based on the {stock_name} and the {positive_sentiment_score} given by the prior agentic crew find the positive news about the stock encouraging investors to buy the stock",
      expected_output="Positive news about the stock encouraging investors to buy the stock",
      agent=self.news_agent()
    )

  @crew
  def crew(self)->Crew:
    return Crew(
      agents=[self.news_agent()],
      tasks=[self.news_task()]
    )




    
