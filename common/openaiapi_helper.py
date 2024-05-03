from dotenv import load_dotenv
import os
import pathway as pw
from pathway.xpacks.llm.embedders import LiteLLMEmbedder
from pathway.xpacks.llm.llms import LiteLLMChat, prompt_chat_single_qa

load_dotenv()

def openai_embedder(data):
    embedder = LiteLLMEmbedder(
        model="voyage/voyage-01",
        api_key=os.environ["VOYAGE_API_KEY"],
        )
    return embedder(data)


def openai_chat_completion(prompt):
    model = LiteLLMChat(
        model="gemini/gemini-pro",
        api_key=os.environ["GEMINI_API_KEY"]
    )

    return model(prompt_chat_single_qa(prompt))
