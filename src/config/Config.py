from functools import lru_cache
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Config(BaseSettings):
    VERSION: str = "0.0.1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_model_name(self):
        model = ""
        return model
    
    def get_model(self):
        model = self.get_model_name()
        company, _, model_name = model.partition(':')
        # match company:
        #     case 'ollama':
        #         return OpenAIModel(
        #             model_name=model_name,
        #             base_url=self.OLLAMA_BASE_URL
        #         )
        #     case 'xai':
        #         return OpenAIModel(
        #             model_name=model_name,
        #             base_url=self.XAI_BASE_URL,
        #             api_key=self.XAI_API_KEY
        #         )
        return model


@lru_cache()
def get_config() -> Config:
    return Config()

config = get_config()
