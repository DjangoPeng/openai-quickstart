from loguru import logger  # 导入loguru库
import os  # 导入os库
import sys  # 导入sys库

LOG_FILE = "translation.log"  # 定义日志文件名
ROTATION_TIME = "02:00"  # 定义日志轮换时间

class Logger:
    # 日志类的构造函数，参数分别为日志名称、日志目录、是否开启debug模式
    def __init__(self, name="translation", log_dir="logs", debug=False):
        if not os.path.exists(log_dir):  # 如果日志目录不存在
            os.makedirs(log_dir)  # 创建日志目录
        log_file_path = os.path.join(log_dir, LOG_FILE)  # 拼接日志文件路径

        logger.remove()  # 移除logger的所有handler

        level = "DEBUG" if debug else "INFO"  # 根据debug参数设置日志级别
        logger.add(sys.stdout, level=level)  # 添加标准输出handler
        logger.add(log_file_path, rotation=ROTATION_TIME, level="DEBUG")  # 添加文件输出handler
        self.logger = logger  # 将logger对象保存到实例变量中

LOG = Logger(debug=True).logger  # 创建Logger实例并获取logger对象

if __name__ == "__main__":
    log = Logger().logger  # 创建Logger实例并获取logger对象

    log.debug("This is a debug message.")  # 输出debug级别的日志
    log.info("This is an info message.")  # 输出info级别的日志
    log.warning("This is a warning message.")  # 输出warning级别的日志
    log.error("This is an error message.")  # 输出error级别的日志