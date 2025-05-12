import yaml
from typing import Iterable, List, Type
from importlib import import_module

class Pipeline:
    def __init__(self, config_path: str):
        with open(config_path, 'r', encoding='utf-8') as f:
            cfg = yaml.safe_load(f)
        self.filters = []
        for name in cfg.get('filters', []):
            module = import_module(f"kwic.filters.{name}")
            # 驼峰拼接，并确保以 Filter 结尾
            base = ''.join(part.capitalize() for part in name.split('_'))
            cls_name = base if base.endswith('Filter') else base + 'Filter'
            cls: Type = getattr(module, cls_name)
            self.filters.append(cls())

    def run(self, lines: Iterable[str]) -> List[str]:
        data = lines
        for filt in self.filters:
            data = filt.process(data)
        return list(data)