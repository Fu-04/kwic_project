import argparse
from kwic.handlers.input_handler import read_input
from kwic.handlers.output_handler import write_to_stdout, write_to_file
from kwic.pipeline import Pipeline

def main():
    parser = argparse.ArgumentParser(description="KWIC 管道-过滤器工具")
    parser.add_argument("-i", "--input", help="输入文件路径，如未指定，则从控制台读取")
    parser.add_argument("-o", "--output", help="输出文件路径，如未指定，则输出到控制台")
    parser.add_argument("-c", "--config", default="pipeline.yml", help="配置文件路径")
    args = parser.parse_args()

    lines = read_input(args.input)
    pipeline = Pipeline(args.config)
    results = pipeline.run(lines)

    if args.output:
        write_to_file(args.output, results)
    else:
        write_to_stdout(results)

if __name__ == "__main__":
    # 建议以模块方式运行：python -m kwic.main
    main()