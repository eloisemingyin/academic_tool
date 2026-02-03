# 🎓 学术Agent - 论文辅助小工具
一款基于阿里云通义千问（Qwen-VL Plus）开发的轻量级学术辅助工具，支持「公式转LaTeX」「图片文本双语互译」「表格识别翻译并导出Excel」，无多余冗余输出，专注学术场景高效使用。

![GitHub top language](https://img.shields.io/github/languages/top/your-username/academic-agent)
![GitHub license](https://img.shields.io/github/license/your-username/academic-agent)
![GitHub last commit](https://img.shields.io/github/last-commit/your-username/academic-agent)

## ✨ 核心功能
1.  **📐 公式识别与转换**
    - 上传公式截图（PNG/JPEG），一键提取为标准LaTeX格式
    - 同时生成可直接粘贴到Word公式编辑器的线性格式，无需手动调整
    - 支持复杂数学公式、物理公式，无多余解释性文字

2.  **🌍 图片文本双语互译（学术级）**
    - 识别图片中的中文/英文文本（支持流程图、论文截图等）
    - 生成逐句对齐的双语对照Markdown表格，方便论文撰写引用
    - 采用学术级翻译风格，避免口语化表达

3.  **📊 表格识别与翻译（保留结构）**
    - 识别图片中的表格结构，还原为标准Markdown表格
    - 支持中英文表格互译，保持原始行列结构不变
    - 支持将翻译后的表格导出为Excel文件（.xlsx），直接用于数据分析

## 🚀 快速开始
### 前置条件
1.  Python 3.8+
2.  阿里云通义千问API Key（[获取地址](https://dashscope.console.aliyun.com/)）
3.  现代浏览器（Chrome/Firefox/Edge，支持SheetJS缓存）

### 环境配置
1.  克隆本仓库
    ```bash
    git clone https://github.com/your-username/academic-agent.git
    cd academic-agent
2.  安装依赖包
    pip install -r requirements.txt
3.  配置 API Key
    打开 app.py，替换其中的 DASHSCOPE_API_KEY 为你的阿里云通义千问 API Key
    DASHSCOPE_API_KEY = "你的通义千问API Key"

### 运行项目
1.  启动 Flask 后端服务
    python app.py
2.  访问工具页面
    打开浏览器，输入地址：http://localhost:5000
    首次加载会缓存 SheetJS（约 500KB），后续使用无需重复加载

### 注意事项

1.  确保你的通义千问 API Key 有足够的额度，避免调用失败
2.  上传的图片需清晰可见，模糊图片可能导致识别精度下降
3.  表格识别支持标准行列结构，复杂合并单元格表格可能识别异常
4.  本地运行仅用于个人学习和科研，请勿用于商业用途

### 许可证
本项目采用 MIT License 开源许可证，详情请查看 LICENSE 文件。
