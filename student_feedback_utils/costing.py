import numpy as np
import requests

def compute_model_cost(response: dict) -> dict:

  # Download model pricing
  url = "https://raw.githubusercontent.com/AgentOps-AI/tokencost/main/tokencost/model_prices.json"
  model_pricing_response = requests.get(url)
  model_pricing_response.raise_for_status()
  model_pricing = model_pricing_response.json()

  # Obtain costs for chosen model
  selected_model = response["model"]
  selected_model_pricing = model_pricing[selected_model]
  selected_model_pricing["prompt_token_price"] = selected_model_pricing["input_cost_per_token"]*1000
  selected_model_pricing["completion_token_price"] = selected_model_pricing["output_cost_per_token"]*1000

  # Compute Cost
  tokens_usage = response["usage"]
  tokens_usage["prompt_token_cost"] = np.ceil(tokens_usage["prompt_tokens"])/1000 * selected_model_pricing["prompt_token_price"]
  tokens_usage["completion_token_cost"] = np.ceil(tokens_usage["completion_tokens"])/1000 * selected_model_pricing["completion_token_price"]
  tokens_usage["total_cost"] = tokens_usage["prompt_token_cost"] + tokens_usage["completion_token_cost"]

  return tokens_usage