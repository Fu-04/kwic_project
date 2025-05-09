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
│   ├── init.py
│   ├── algorithms.py           # 核心算法模块
│   ├── handlers/               # 输入输出处理器
│   │   ├── init.py
│   │   ├── input_handler.py    # 控制台与文件输入处理
│   │   └── output_handler.py   # 控制台与文件输出处理
│   ├── filters/                # 过滤器模块
│   │   ├── init.py
│   │   ├── circular_shifter.py # 循环移位过滤器
│   │   ├── sorter.py           # 排序过滤器
│   │   ├── punctuation_filter.py # 标点过滤插件
│   │   └── sensitive_filter.py # 敏感词过滤插件
│   ├── api.py                  # FastAPI 接口
│   ├── pipeline.py             # 管道管理与执行入口
│   └── main.py                 # 脚本入口
├── pipeline.yml                # 过滤器配置示例
├── requirements.txt            # 依赖清单
└── README.md                   # 项目说明文档


## 安装

```bash
git clone https://github.com/Fu-04/kwic_project
cd kwic_project
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
pip install -r requirements.txt
