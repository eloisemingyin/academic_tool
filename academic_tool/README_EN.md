# 🎓 Academic Agent - Academic Assistant Tool
A lightweight academic assistant tool developed based on Alibaba Cloud DashScope (Qwen-VL Plus), supporting "Formula to LaTeX", "Image Text Bilingual Translation", and "Table Recognition Translation with Excel Export". No redundant output, focusing on efficient use in academic scenarios.

![GitHub top language](https://img.shields.io/github/languages/top/your-username/academic-agent)
![GitHub license](https://img.shields.io/github/license/your-username/academic-agent)
![GitHub last commit](https://img.shields.io/github/last-commit/your-username/academic-agent)

## ✨ Core Features
1.  **📐 Formula Recognition and Conversion**
    - Upload formula screenshots (PNG/JPEG) and extract them into standard LaTeX format with one click
    - Generate linear format that can be directly pasted into Word Formula Editor without manual adjustment
    - Support complex mathematical and physical formulas with no redundant explanatory text

2.  **🌍 Academic-Level Bilingual Translation of Image Text**
    - Recognize Chinese/English text in images (support flowcharts, paper screenshots, etc.)
    - Generate sentence-aligned bilingual comparison Markdown tables for easy citation in paper writing
    - Adopt academic translation style to avoid colloquial expressions

3.  **📊 Table Recognition and Translation (Structure Preserved)**
    - Recognize table structures in images and restore them to standard Markdown tables
    - Support Chinese-English table mutual translation while maintaining the original row and column structure
    - Support exporting translated tables as Excel files (.xlsx) for direct use in data analysis

## 🚀 Quick Start
### Prerequisites
1.  Python 3.8+
2.  Alibaba Cloud DashScope API Key ([Get it here](https://dashscope.console.aliyun.com/))
3.  Modern browser (Chrome/Firefox/Edge, supporting SheetJS caching)

### Environment Configuration
1.  Clone this repository
    ```bash
    git clone https://github.com/your-username/academic-agent.git
    cd academic-agent
2.  Install dependent packages
    run“pip install -r requirements.txt”
3.  Configure API Key
    Open app.py and replace the DASHSCOPE_API_KEY with your own Alibaba Cloud DashScope API Key
    DASHSCOPE_API_KEY = "Your DashScope API Key"

### Run the Project
1.  Start the Flask backend service
    run “python app.py”
2.  Access the tool page
    Open your browser and enter the address: http://localhost:5000
    SheetJS (about 500KB) will be cached on the first load, no repeated loading for subsequent use

### 注意事项

1.  Ensure that your DashScope API Key has sufficient quota to avoid call failures
2.  Uploaded images must be clear; blurry images may lead to reduced recognition accuracy
3.  Table recognition supports standard row and column structures; complex merged cell tables may be recognized abnormally
4.  Local operation is only for personal study and scientific research, not for commercial use

### 许可证
This project is licensed under the MIT License. Please see the LICENSE file for details.
