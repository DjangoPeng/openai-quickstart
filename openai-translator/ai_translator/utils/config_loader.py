# 导入yaml模块，用于读取和解析YAML文件
import yaml

# 定义 ConfigLoader 类
class ConfigLoader:
    # 初始化方法，接收配置文件路径参数
    def __init__(self, config_path):
        self.config_path = config_path

    # 加载配置文件的方法
    def load_config(self):
        # 打开配置文件
        with open(self.config_path, "r") as f:
            # 使用 yaml 库加载配置文件内容
            config = yaml.safe_load(f)
        # 返回配置文件内容
        return config