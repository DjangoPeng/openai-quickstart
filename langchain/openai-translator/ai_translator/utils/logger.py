from loguru import logger  # 导入loguru模块中的logger类，用于日志处理
import os  # 导入os模块，用于文件操作
import sys  # 导入sys模块，用于获取命令行参数

LOG_FILE = "translation.log"  # 定义日志文件名
ROTATION_TIME = "02:00"  # 定义日志轮换时间

class Logger:
    # 定义Logger类，用于日志处理，包括控制台和文件两种处理方式
    # 参数：
    #   name: 日志名称
    #   log_dir: 日志目录
    #   debug: 是否开启debug模式
    def __init__(self, name="translation", log_dir="logs", debug=False):
        if not os.path.exists(log_dir):  # 如果日志目录不存在，则创建
            os.makedirs(log_dir)
        log_file_path = os.path.join(log_dir, LOG_FILE)  # 拼接日志文件路径

        # 移除默认的loguru处理方式
        logger.remove()

        # 添加控制台处理，设置特定的日志级别
        level = "DEBUG" if debug else "INFO"
        logger.add(sys.stdout, level=level)

        # 添加文件处理，设置特定的日志级别和定时轮换
        logger.add(log_file_path, rotation=ROTATION_TIME, level="DEBUG")
        self.logger = logger

LOG = Logger(debug=True).logger  # 创建Logger实例并获取logger对象

if __name__ == "__main__":
    log = Logger().logger  # 创建Logger实例并获取logger对象

    log.debug("This is a debug message.")  # 输出debug级别的日志信息
    log.info("This is an info message.")  # 输出info级别的日志信息
    log.warning("This is a warning message.")  # 输出warning级别的日志信息
    log.error("This is an error message.")  # 输出error级别的日志信息