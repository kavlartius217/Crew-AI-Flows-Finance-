from crewai import Agent, Task, Crew
from crewai.project import agent, task, crew, CrewBase
from crewai_tools import SerperDevTool

search_tool_1= SerperDevTool()

@CrewBase
class insights_crew():
  
  @agent
  def insight_agent(self)->Agent:
    return Agent(
      role="Insight based information provider",
      goal="Provide useful inferences and insights which would help an investor based on the past data of a stock",
      backstory="You are share holder with years of experience and an expertise on evaluating past stock metrics drawing inferences for future actions",
      tools=[search_tool_1]
    )

  
  @task
  def insights_task(self)->Task:
    return Task(
      description="Given the {stock_name} and its {negative_sentiment_score} determined by the prior agentic crew, analyze the stock tables for the past 6 months. Provide strategic insights on how an investor can turn a profit despite the current negative sentiment.",
      expected_output="Actionable insights derived from the past 6 months of {stock_name} stock data, considering its bad sentiment analysis score. Offer strategies to help the investor capitalize on this scenario and generate profit.", 
      agent=self.insight_agent()
    )

  
  @crew
  def crew(self)->Crew:
    return Crew(
      agents=[self.insight_agnet()],
      tasks=[self.insights_task()]
    )
