# TradingAgents DeepSeek 集成指南

本文档介绍如何在 TradingAgents 框架中使用 DeepSeek 大模型。

## 1. 配置 DeepSeek

### 方法一：使用环境变量

1. 复制 `.env.example` 文件为 `.env`：
```bash
cp .env.example .env
```

2. 在 `.env` 文件中添加您的 DeepSeek API 密钥：
```
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

### 方法二：在代码中直接配置

在您的代码中直接设置配置：

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 创建使用DeepSeek的配置
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "deepseek"
config["deep_think_llm"] = "deepseek-chat"
config["quick_think_llm"] = "deepseek-chat"
config["backend_url"] = "https://api.deepseek.com/v1"
config["deepseek_api_key"] = "your_deepseek_api_key_here"  # 可选，也可以使用环境变量

# 初始化TradingAgentsGraph
ta = TradingAgentsGraph(debug=True, config=config)
```

## 2. 修改 main.py 使用 DeepSeek

在 `main.py` 中，取消注释 DeepSeek 相关配置行：

```python
# Create a custom config
config = DEFAULT_CONFIG.copy()

# 选择LLM提供商: "openai", "anthropic", "google", "deepseek"
config["llm_provider"] = "deepseek"  # 使用DeepSeek

# DeepSeek配置
config["deep_think_llm"] = "deepseek-chat"
config["quick_think_llm"] = "deepseek-chat"
config["backend_url"] = "https://api.deepseek.com/v1"

# OpenAI配置 (注释掉)
# config["llm_provider"] = "openai"
# config["deep_think_llm"] = "gpt-4o-mini"
# config["quick_think_llm"] = "gpt-4o-mini"

config["max_debate_rounds"] = 1

# Configure data vendors
config["data_vendors"] = {
    "core_stock_apis": "yfinance",
    "technical_indicators": "yfinance",
    "fundamental_data": "alpha_vantage",
    "news_data": "alpha_vantage",
}

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)
```

## 3. 测试 DeepSeek 集成

运行测试脚本验证 DeepSeek 集成是否正常工作：

```bash
python test_deepseek.py
```

## 4. 支持的 DeepSeek 模型

目前支持以下 DeepSeek 模型：

- `deepseek-chat`: DeepSeek 的通用对话模型
- `deepseek-coder`: DeepSeek 的代码专用模型

## 5. 注意事项

1. **API 密钥安全**: 请妥善保管您的 DeepSeek API 密钥，不要将其提交到版本控制系统
2. **成本考虑**: DeepSeek 通常比 OpenAI 模型更经济，适合大规模使用
3. **性能差异**: 不同模型的性能特点可能不同，可能需要调整提示词或参数
4. **API 限制**: 注意 DeepSeek API 的调用频率限制

## 6. 故障排除

### 常见问题

1. **API 密钥错误**:
   - 确保已正确设置 `DEEPSEEK_API_KEY` 环境变量
   - 检查 API 密钥是否有效

2. **模块导入错误**:
   - 确保已安装所有依赖：`pip install -r requirements.txt`
   - 确保已安装 `python-dotenv`：`pip install python-dotenv`

3. **网络连接问题**:
   - 检查网络连接
   - 确认可以访问 DeepSeek API 端点

### 调试模式

启用调试模式查看详细日志：

```python
ta = TradingAgentsGraph(debug=True, config=config)
```

## 7. 与其他 LLM 提供商切换

您可以在不同 LLM 提供商之间轻松切换：

```python
# 使用 OpenAI
config["llm_provider"] = "openai"
config["deep_think_llm"] = "gpt-4o-mini"
config["quick_think_llm"] = "gpt-4o-mini"

# 使用 DeepSeek
config["llm_provider"] = "deepseek"
config["deep_think_llm"] = "deepseek-chat"
config["quick_think_llm"] = "deepseek-chat"

# 使用 Anthropic
config["llm_provider"] = "anthropic"
config["deep_think_llm"] = "claude-3-sonnet-20240229"
config["quick_think_llm"] = "claude-3-haiku-20240307"
```

## 8. 贡献

如果您发现问题或有改进建议，请提交 Issue 或 Pull Request。