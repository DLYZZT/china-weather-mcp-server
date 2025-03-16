# China Weather MCP Server

[English](#english) | [中文](#chinese)

<a name="english"></a>
## English

### Introduction
China Weather MCP Server is a Model Context Protocol (MCP) server that provides real-time weather information for Chinese cities using the AMap (AutoNavi) Weather API. This server enables AI assistants to access current weather conditions across China.

### Features
- Real-time weather data retrieval for Chinese cities
- Integration with AMap Weather API
- Asynchronous request handling
- Easy-to-use MCP interface

### Installation
1. Ensure Python 3.12 or higher is installed
2. Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
3. Clone this repository:
```bash
git clone https://github.com/DLYZZT/china-weather-mcp-server.git
cd china-weather-mcp-server
```
4. Install dependencies with uv:
```bash
uv pip install .
```

### Configuration
1. Get an API key from [AMap Developer Platform](https://lbs.amap.com/)
2. Set your API key as an environment variable:
```bash
export AMAP_API_KEY="your_api_key_here"
```

### Usage
To use with Claude Desktop, add the following configuration to your Claude Desktop config file:

On Windows: `%APPDATA%/Claude/claude_desktop_config.json`
On MacOS: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "path/china-weather-mcp-server",
        "run",
        "weather.py"
      ],
      "env": {
        "AMAP_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

The server provides the following tool:
- `get_weather(city: str)`: Get current weather information for a specified Chinese city

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<a name="chinese"></a>
## 中文

### 简介
中国天气 MCP 服务器是一个基于模型上下文协议（Model Context Protocol，MCP）的服务器，使用高德地图天气 API 提供中国城市的实时天气信息。该服务器使 AI 助手能够访问中国各地的当前天气状况。

### 特性
- 获取中国城市的实时天气数据
- 集成高德地图天气 API
- 异步请求处理
- 简单易用的 MCP 接口

### 安装方法
1. 确保已安装 Python 3.12 或更高版本
2. 安装 uv：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
3. 克隆此仓库：
```bash
git clone https://github.com/DLYZZT/china-weather-mcp-server.git
cd china-weather-mcp-server
```
4. 使用 uv 安装依赖：
```bash
uv pip install .
```

### 配置
1. 从[高德开放平台](https://lbs.amap.com/)获取 API 密钥
2. 设置 API 密钥环境变量：
```bash
export AMAP_API_KEY="你的API密钥"
```

### 使用方法
要在 Claude Desktop 中使用，请在 Claude Desktop 配置文件中添加以下配置：

Windows系统：`%APPDATA%/Claude/claude_desktop_config.json`
MacOS系统：`~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "weather": {
      "command": "uv",
      "args": [
        "--directory",
        "path/china-weather-mcp-server",
        "run",
        "weather.py"
      ],
      "env": {
        "AMAP_API_KEY": "你的API密钥"
      }
    }
  }
}
```

服务器提供以下工具：
- `get_weather(city: str)`：获取指定中国城市的当前天气信息

### 许可证
本项目采用 MIT 许可证 - 详情请参见 [LICENSE](LICENSE) 文件。
