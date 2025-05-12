# KWIC 管道-过滤器项目

实现 Key Word In Context (KWIC) 功能，采用 **管道-过滤器** 架构。

## 特性
- 循环移位（Circular Shifts）
- 自定义排序（空格优先、小写优先）
- 控制台输入/输出
- 可插拔过滤器模块
- 命令行工具 & FastAPI 接口
- 包内资源敏感词库，默认无需额外配置

## 目录结构
kwic_project/                     # 项目根目录
├── kwic/                        # 主包目录，所有核心逻辑均在此
│   ├── __init__.py              # 包声明文件
│   ├── algorithms.py            # 核心算法：循环移位 & 排序键生成
│   ├── handlers/                # I/O 处理模块
│   │   ├── __init__.py          # 包声明
│   │   ├── input_handler.py     # 从文件或标准输入读取文本行
│   │   └── output_handler.py    # 将结果输出到控制台或写入文件
│   ├── filters/                 # “过滤器”模块目录，可插拔式设计
│   │   ├── __init__.py          # 包声明 & 可能的资源清单
│   │   ├── circular_shifter.py  # 循环移位过滤器：生成所有移位行
│   │   ├── punctuation_filter.py# （可选）标点过滤器：移除或保留标点
│   │   ├── sensitive_filter.py  # 敏感词过滤器：替换 / 屏蔽敏感词
│   │   ├── trie.py              # 字典树实现，用于高效敏感词匹配
│   │   └── json.json            # 包内默认敏感词库（随包发布的资源）
│   ├── api.py                   # FastAPI 接口定义，暴露 `/kwic` 路由
│   ├── pipeline.py              # 管道管理：读取配置、串联过滤器
│   └── main.py                  # 脚本入口：命令行参数解析 & 调度
├── pipeline.yml                 # YAML 配置：定义要启用及顺序的过滤器
├── requirements.txt             # Python 依赖列表（PyYAML, fastapi, uvicorn…）
├── README.md                    # 项目说明文档（安装、示例、资源管理等）
└── demo_input.txt               # 示例输入文件，用于命令行快速测试

## 安装
```bash
git clone https://github.com/Fu-04/kwic_project
cd kwic_project
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
