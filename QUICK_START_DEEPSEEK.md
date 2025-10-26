# DeepSeek 快速开始指南

本指南将帮助您快速配置和使用 DeepSeek 大模型与 TradingAgents 框架。

## 🚀 快速配置步骤

### 1. 获取 DeepSeek API 密钥

1. 访问 [DeepSeek 官网](https://www.deepseek.com/)
2. 注册并登录账户
3. 前往 API 管理页面获取您的 API 密钥

### 2. 配置环境变量

创建 `.env` 文件（如果不存在）并添加以下内容：

```bash
# DeepSeek API 配置
DEEPSEEK_API_KEY=your_api_key_here
```

或者，您可以直接在代码中配置：

```python
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "deepseek"
config["deepseek_deep_think_llm"] = "deepseek-reasoner"
config["deepseek_quick_think_llm"] = "deepseek-chat"
config["deepseek_api_key"] = "your_api_key_here"
```

### 3. 安装依赖

使用国内镜像源加速安装：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple langchain-openai langchain-experimental langgraph pandas yfinance python-dotenv
```

### 4. 测试集成

运行测试脚本验证配置：

```bash
python test_deepseek_integration.py
```

## 📋 可用模型

DeepSeek 提供以下模型：

- `deepseek-chat`: 通用对话模型，适用于大多数任务
- `deepseek-coder`: 代码专用模型，适用于代码相关任务

## 🔧 高级配置

### 自定义后端 URL

如果需要使用自定义后端：

```python
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "deepseek"
config["deepseek_backend_url"] = "https://your-custom-backend.com"
config["deepseek_api_key"] = "your_api_key_here"
```

### 模型参数调整

```python
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "deepseek"
config["deepseek_deep_think_llm"] = "deepseek-reasoner"
config["deepseek_quick_think_llm"] = "deepseek-chat"
config["temperature"] = 0.1  # 控制随机性，0-1之间
config["max_tokens"] = 2000  # 最大生成令牌数
```

## 🎯 使用示例

### 基本使用

```python
from tradingagents.graph.trading_graph import TradingGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 配置 DeepSeek
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "deepseek"
config["deepseek_deep_think_llm"] = "deepseek-reasoner"
config["deepseek_quick_think_llm"] = "deepseek-chat"

# 创建交易图
trading_graph = TradingGraph(config)

# 运行分析
result = trading_graph.run_analysis("AAPL")
print(result)
```

### 直接使用 DeepSeek API

```python
from langchain_openai import ChatOpenAI
import os

# 创建 DeepSeek 客户端
llm = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com",
    openai_api_key=os.getenv("DEEPSEEK_API_KEY"),
    temperature=0.1
)

# 发送请求
response = llm.invoke("分析一下苹果公司的股票前景")
print(response.content)
```

## 🛠️ 故障排除

### 常见问题

1. **API 密钥错误**
   - 确保 `.env` 文件中的 `DEEPSEEK_API_KEY` 正确
   - 检查 API 密钥是否有效且未过期

2. **网络连接问题**
   - 尝试使用国内镜像源安装依赖
   - 检查防火墙设置

3. **模型不可用**
   - 确认使用的模型名称正确（`deepseek-chat` 或 `deepseek-coder`）
   - 检查 DeepSeek 服务状态

### 调试模式

启用详细日志：

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📚 更多资源

- [DeepSeek 官方文档](https://platform.deepseek.com/)
- [TradingAgents 项目文档](README.md)
- [LangChain 文档](https://python.langchain.com/)

## 🆘 获取帮助

如果遇到问题，请：

1. 检查 [TROUBLESHOOTING.md](TROUBLESHOOTING.md) 文件
2. 运行 `python test_deepseek_integration.py` 进行诊断
3. 查看项目 Issues 页面

---

🎉 现在您已经准备好使用 DeepSeek 大模型进行智能交易分析了！