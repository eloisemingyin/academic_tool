from flask import Flask, request, jsonify, send_from_directory
import dashscope
from dashscope import MultiModalConversation
from werkzeug.utils import secure_filename
import traceback
from PIL import Image
import io
import base64

# ================== API_Key配置 ==================
DASHSCOPE_API_KEY = "Your DashScope API Key"
# ==========================================

app = Flask(__name__)
dashscope.api_key = DASHSCOPE_API_KEY


@app.route('/')
def home():
    #index.html 在 app.py 同目录
    return send_from_directory('.', 'index.html')


@app.route('/process-image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': '缺少 image 文件'}), 400
    
    file = request.files['image']
    task = request.form.get('task', 'general')
    
    if file.filename == '':
        return jsonify({'error': '文件名为空'}), 400

    # 读取原始字节用于验证
    try:
        file_bytes = file.read()
        if len(file_bytes) == 0:
            return jsonify({'error': '上传的文件为空'}), 400

        # 验证是否为有效图像
        img = Image.open(io.BytesIO(file_bytes))
        img.verify()  # 抛出异常如果非图像或损坏
    except Exception as e:
        print("❌ 图像验证失败:", str(e))
        return jsonify({'error': '图片格式无效或已损坏，请上传 PNG/JPG/BMP 等标准图像'}), 400

    # ========== 关键：使用 Base64 直接传输 ==========
    # 重置文件指针以重新读取原始数据
    file.seek(0)
    original_data = file.read()

    # 自动判断 MIME 类型
    filename_lower = file.filename.lower()
    if filename_lower.endswith(('.jpg', '.jpeg')):
        mime_type = 'image/jpeg'
    else:
        mime_type = 'image/png'  # 默认用 PNG（支持透明，通用）

    # 编码为 Base64
    encoded_str = base64.b64encode(original_data).decode('utf-8')
    image_url = f"data:{mime_type};base64,{encoded_str}"

    # ==================prompts==========================
    prompts = {
        'formula': "请将图中的数学公式转换为标准 LaTeX 格式，并同时提供 Word 公式编辑器可用的线性格式。",
        'translate_zh2en': "请将图中的中文内容翻译成专业、流畅的英文学术语言。",
        'translate_en2zh': "请将图中的英文内容翻译成专业、流畅的中文学术语言。",
        'ocr_only': (
            "【严格模式】仅输出原始文字内容，不要任何解释、标题、前缀或后缀。"
            "保留原始分行，不要添加额外空行或符号。"
        ),
        'table_ocr_only': (
            "【严格模式】仅输出标准 Markdown 表格，不要任何前缀、后缀、说明、标题或解释。"
            "第一行必须是 | 列1 | 列2 | ... |，第二行是分隔线 |---|---|...|。"
            "不要输出 '表格如下：'、'识别结果：' 等任何额外文字。"
        ),
        'table_translate_zh2en': "请将图中的表格内容识别出来，并将其从中文翻译成专业、流畅的英文学术语言，然后以Markdown表格格式输出，保持原始行列结构。",
        'table_translate_en2zh': "请将图中的表格内容识别出来，并将其从英文翻译成专业、流畅的中文学术语言，然后以Markdown表格格式输出，保持原始行列结构。",
    }
    
    prompt_text = prompts.get(task, "请描述图中的内容。")

    try:
        messages = [{
            "role": "user",
            "content": [
                {"image": image_url},  # ← Base64 字符串，非 URL！
                {"text": prompt_text}
            ]
        }]

        response = MultiModalConversation.call(
            model='qwen-vl-plus',
            messages=messages
        )

        print("📡 DashScope 响应状态码:", response.status_code)

        if response.status_code != 200:
            return jsonify({
                'error': f'API 错误: {response.code} - {response.message}',
                'request_id': getattr(response, 'request_id', 'N/A')
            }), 500

        if not response.output or not hasattr(response.output, 'choices'):
            return jsonify({'error': 'AI 返回空结果'}), 500

        result = response.output.choices[0].message.content[0]['text'].strip()
        return jsonify({'result': result})

    except Exception as e:
        print("💥 调用 AI 时发生异常:")
        traceback.print_exc()
        return jsonify({'error': f'处理异常: {str(e)}'}), 500


# 注意：不再需要 /uploads/<filename> 路由！

if __name__ == '__main__':
    print("✅ 启动服务:http://localhost:5000")
    print("💡 图片通过 Base64 直接传输。")
    app.run(host='0.0.0.0', port=5000, debug=False)  # 关闭 debug