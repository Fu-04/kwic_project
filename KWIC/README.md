# KWIC 管道-过滤器项目

实现 Key Word In Context (KWIC) 功能，采用 **管道-过滤器** 架构。

## 特性
- 循环移位（Circular Shifts）
- 自定义排序（空格优先、小写优先）
- 控制台输入/输出
- 可插拔过滤器模块
- 命令行工具 & FastAPI 接口

## 目录结构
kwic_project/
├── kwic/
│   ├── algorithms.py
│   ├── filters/
│   │   ├── circular_shifter.py
│   │   └── sorter.py
│   ├── input.py
│   ├── output.py
│   ├── api.py
│   └── main.py
├── requirements.txt
└── README.md


## 安装

```bash
git clone <repo_url>
cd kwic_project
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
pip install -r requirements.txt