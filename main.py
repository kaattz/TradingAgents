from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a custom config
config = DEFAULT_CONFIG.copy()
# 选择LLM提供商: "openai", "anthropic", "google", "deepseek"
config["llm_provider"] = "openai"  # 可以改为 "deepseek" 来使用DeepSeek

# OpenAI配置
config["deep_think_llm"] = "gpt-4o-mini"  # Use a different model
config["quick_think_llm"] = "gpt-4o-mini"  # Use a different model

# DeepSeek配置 (如果使用DeepSeek，取消注释下面的行)
# config["llm_provider"] = "deepseek"
# config["deep_think_llm"] = "deepseek-chat"
# config["quick_think_llm"] = "deepseek-chat"
# config["backend_url"] = "https://api.deepseek.com/v1"

config["max_debate_rounds"] = 1  # Increase debate rounds

# Configure data vendors (default uses yfinance and alpha_vantage)
config["data_vendors"] = {
    "core_stock_apis": "yfinance",           # Options: yfinance, alpha_vantage, local
    "technical_indicators": "yfinance",      # Options: yfinance, alpha_vantage, local
    "fundamental_data": "alpha_vantage",     # Options: openai, alpha_vantage, local
    "news_data": "alpha_vantage",            # Options: openai, alpha_vantage, google, local
}

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
