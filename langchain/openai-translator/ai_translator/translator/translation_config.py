import yaml  # 导入yaml模块，用于读取和解析YAML文件

# 定义TranslationConfig类，用于存储翻译配置
class TranslationConfig:
    _instance = None
    
    def __new__(cls):
        # 如果类的_instance属性为空，则创建一个新的实例
        if cls._instance is None:
            cls._instance = super(TranslationConfig, cls).__new__(cls)
            # 初始化_config属性为空
            cls._instance._config = None
        return cls._instance
    
    # 初始化_config属性，参数args是argparse.Namespace对象
    def initialize(self, args):
        # 从配置文件中读取配置
        with open(args.config_file, "r") as f:
            config = yaml.safe_load(f)

        # 使用argparse Namespace更新配置
        overridden_values = {
            key: value for key, value in vars(args).items() if key in config and value is not None
        }
        config.update(overridden_values)    
        
        # 存储配置
        self._instance._config = config

    def __getattr__(self, name):
        # 尝试从_config中获取属性
        if self._instance._config and name in self._instance._config:
            return self._instance._config[name]
        # 如果属性不存在，则抛出AttributeError
        raise AttributeError(f"'TranslationConfig' object has no attribute '{name}'")