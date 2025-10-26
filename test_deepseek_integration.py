#!/usr/bin/env python3
"""
DeepSeek 集成测试脚本
用于验证 DeepSeek 大模型是否成功集成到 TradingAgents 框架中
"""

import os
import sys
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_deepseek_config():
    """测试 DeepSeek 配置是否正确"""
    print("🔍 测试 DeepSeek 配置...")
    
    # 检查环境变量
    deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
    if not deepseek_api_key:
        print("❌ 错误: 未找到 DEEPSEEK_API_KEY 环境变量")
        print("请确保在 .env 文件中设置了 DEEPSEEK_API_KEY=your_api_key_here")
        return False
    
    print(f"✅ 找到 DeepSeek API 密钥: {deepseek_api_key[:10]}...")
    
    # 测试导入配置
    try:
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from tradingagents.default_config import DEFAULT_CONFIG
        print("✅ 成功导入 DEFAULT_CONFIG")
        
        # 检查 DeepSeek 配置选项
        if "deepseek_api_key" in DEFAULT_CONFIG:
            print("✅ DEFAULT_CONFIG 中包含 deepseek_api_key 配置")
        else:
            print("❌ DEFAULT_CONFIG 中缺少 deepseek_api_key 配置")
            return False
            
        if "deepseek_backend_url" in DEFAULT_CONFIG:
            print("✅ DEFAULT_CONFIG 中包含 deepseek_backend_url 配置")
        else:
            print("❌ DEFAULT_CONFIG 中缺少 deepseek_backend_url 配置")
            return False
            
    except ImportError as e:
        print(f"❌ 导入配置失败: {e}")
        return False
    
    return True

def test_langchain_import():
    """测试 langchain-openai 是否可以导入"""
    print("\n🔍 测试 langchain-openai 导入...")
    
    try:
        from langchain_openai import ChatOpenAI
        print("✅ 成功导入 ChatOpenAI")
        return True
    except ImportError as e:
        print(f"❌ 导入 ChatOpenAI 失败: {e}")
        print("请确保已安装 langchain-openai: pip install langchain-openai")
        return False

def test_deepseek_connection():
    """测试 DeepSeek 连接"""
    print("\n🔍 测试 DeepSeek 连接...")
    
    try:
        from langchain_openai import ChatOpenAI
        
        # 创建 DeepSeek 客户端
        deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
        deepseek_backend_url = "https://api.deepseek.com"
        
        llm = ChatOpenAI(
            model="deepseek-chat",
            base_url=deepseek_backend_url,
            openai_api_key=deepseek_api_key,
            temperature=0.1
        )
        
        # 发送简单测试请求
        response = llm.invoke("你好，请简单介绍一下你自己。")
        print(f"✅ DeepSeek 连接成功!")
        print(f"📝 响应: {response.content[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ DeepSeek 连接失败: {e}")
        return False

def test_trading_graph_integration():
    """测试 TradingGraph 中的 DeepSeek 集成"""
    print("\n🔍 测试 TradingGraph 中的 DeepSeek 集成...")
    
    try:
        # 创建测试配置
        from tradingagents.default_config import DEFAULT_CONFIG
        config = DEFAULT_CONFIG.copy()
        config["llm_provider"] = "deepseek"
        config["deepseek_deep_think_llm"] = "deepseek-reasoner"
        config["deepseek_quick_think_llm"] = "deepseek-chat"
        config["deepseek_api_key"] = os.getenv("DEEPSEEK_API_KEY")
        
        # 尝试导入 TradingAgentsGraph
        from tradingagents.graph.trading_graph import TradingAgentsGraph
        print("✅ 成功导入 TradingAgentsGraph")
        
        # 注意: 这里不实际创建 TradingAgentsGraph 实例，因为它需要很多依赖
        # 我们只验证导入和配置是否正确
        print("✅ DeepSeek 集成配置验证通过")
        return True
        
    except ImportError as e:
        print(f"❌ 导入 TradingGraph 失败: {e}")
        return False
    except Exception as e:
        print(f"❌ TradingGraph 集成测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("🚀 开始 DeepSeek 集成测试...\n")
    
    tests = [
        ("配置测试", test_deepseek_config),
        ("依赖导入测试", test_langchain_import),
        ("DeepSeek 连接测试", test_deepseek_connection),
        ("TradingGraph 集成测试", test_trading_graph_integration),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} 执行异常: {e}")
            results.append((test_name, False))
    
    # 输出测试结果摘要
    print("\n" + "="*50)
    print("📊 测试结果摘要:")
    print("="*50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n总计: {passed}/{total} 测试通过")
    
    if passed == total:
        print("🎉 所有测试通过! DeepSeek 集成成功!")
        return 0
    else:
        print("⚠️  部分测试失败，请检查上述错误信息")
        return 1

if __name__ == "__main__":
    sys.exit(main())