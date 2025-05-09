import sys
from kwic.pipeline import KWICPipeline


def main():
    # 接收可选的输入和输出路径参数
    args = sys.argv[1:]
    source = args[0] if len(args) > 0 else None
    dest   = args[1] if len(args) > 1 else None

    pipeline = KWICPipeline(source, dest)
    pipeline.run()

if __name__ == '__main__':
    main()