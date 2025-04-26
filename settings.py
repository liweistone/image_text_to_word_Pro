import os

# 基础路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 输入输出目录
INPUT_DIR = os.path.join(BASE_DIR, "input_files")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# 支持的文件类型
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
TEXT_EXTENSION = '.txt'

# 自动创建目录
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)