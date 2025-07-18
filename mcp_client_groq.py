import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq # Import ChatGroq
from mcp_use import MCPAgent, MCPClient
from src.schemas.car import CarFilterSchema
import os


load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
VERBOSE = bool(os.getenv('VERBOSE', "FALSE").upper() == "TRUE")

if not API_KEY:
    print("No API key found, exiting !!!!!")
    quit


async def main():
    mcp_config = {
        "mcpServers": {
            "mcp_server_cars": {
                "command": "python",
                "args": ["mcp_server.py"]
            }
        }
    }

    client = MCPClient.from_dict(config=mcp_config)

    llm = ChatGroq(
        temperature=0,
        groq_api_key=API_KEY,
        model_name="llama3-8b-8192"
    )
    agent = MCPAgent(llm=llm, client=client, verbose=False, max_steps=30, disallowed_tools=["network", "shell"])

    attributes = ""
    for field in CarFilterSchema.model_fields.keys():
        attributes += f'- {field} \n'
    print(
        "Hello there! \n Let's find your new car?\n" \
        f" Ask me for a car using any of those characteristics: \n {attributes}" \
        " Or just type exit :("
    )
    while True:
        user_input = input("\n?: ")
        if user_input.lower() == "exit":
            break
        try:
            response = await agent.run(query=user_input)
            print(response)
        except Exception as e:
            print(f"\n :( something wrong it's not right !\n {e}")

if __name__ == "__main__":
    asyncio.run(main())