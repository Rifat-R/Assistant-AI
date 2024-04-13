from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI
import os
from dotenv import load_dotenv
from asana_function import AsanaFunctions

load_dotenv()

asana_functions = AsanaFunctions(file_path='data.json')
function_tools = asana_functions.function_tools


# Im not entirely sure how os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") works, 
# but llamaindex needs environment variables to be set in order to work
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = OpenAI(model="gpt-3.5-turbo-1106")
agent = OpenAIAgent.from_tools(
    function_tools, llm=llm, verbose=True
)

response = agent.chat("What projects are there?")



if __name__ == "__main__":
    while True:
        query = input("Enter your query: ")
        response = agent.chat(query)
        print(str(response))