from openai import OpenAI
from app.config import settings
from typing import List, Dict, Any, Optional
import json


class LLMClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.llm_api_key,
            base_url=settings.llm_base_url
        )
        self.model = settings.llm_model
    
    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        tools: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.7
    ) -> Dict[str, Any]:
        """
        Call LLM with optional tool calling support
        """
        try:
            kwargs = {
                "model": self.model,
                "messages": messages,
                "temperature": temperature,
            }
            
            if tools:
                kwargs["tools"] = tools
                kwargs["tool_choice"] = "auto"
            
            response = self.client.chat.completions.create(**kwargs)
            return response
        except Exception as e:
            print(f"LLM Error: {e}")
            raise
    
    def parse_tool_calls(self, response) -> List[Dict[str, Any]]:
        """
        Extract tool calls from LLM response
        """
        tool_calls = []
        message = response.choices[0].message
        
        if hasattr(message, 'tool_calls') and message.tool_calls:
            for tool_call in message.tool_calls:
                tool_calls.append({
                    "id": tool_call.id,
                    "name": tool_call.function.name,
                    "arguments": json.loads(tool_call.function.arguments)
                })
        
        return tool_calls
    
    def get_text_response(self, response) -> str:
        """
        Extract text content from LLM response
        """
        return response.choices[0].message.content or ""


llm_client = LLMClient()
