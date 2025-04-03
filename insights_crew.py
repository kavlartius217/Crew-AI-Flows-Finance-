from crewai import Agent, Task, Crew, Process
from crewai.project import agent, task, crew, CrewBase
from crewai_tools import SerperDevTool

search_tool=SerperDevTool()

@CrewBase
class sentiment_crew():

  @agent
  def sentiment_analysis_agent(self)->Agent:
    return Agent(
       role="Stock Public Sentiment Analysis",
       goal="Analyze the public sentiment of a stock and assign a score",
       backstory="You are an expert in researching and analyzing public sentiments in the stock name",
       tools=[search_tool]
    )

  @task
  def sentiment_analysis_task(self)->Task:
    return Task(
      description=" based on the {stock_name} provided by the user analyze the current news about the stock and assign a score 1- negative, 2- neutral, 3-negative",
      expected_output="A sentiment analysis score with no further texts or outputs",
      agent=self.sentiment_analysis_agent()
    )


  def crew(self)->Crew:
    return Crew(
      agents=[self.sentiment_analysis_agent()],
      tasks=[self.sentiment_analysis_task()]
    )
