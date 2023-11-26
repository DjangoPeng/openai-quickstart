import pandas as pd  # 导入 pandas 库，用于处理表格数据

from enum import Enum, auto  # 导入枚举类和自动编号功能，用于定义 ContentType 枚举类
from PIL import Image as PILImage  # 导入 PIL 库中的 Image 类并重命名为 PILImage，用于处理图像数据
from utils import LOG  # 导入 utils 模块中的 LOG 对象，用于输出调试信息
from io import StringIO  # 导入 StringIO 类，用于将字符串转换为文件对象

class ContentType(Enum):  # 定义 ContentType 枚举类
    TEXT = auto()  # 文本类型
    TABLE = auto()  # 表格类型
    IMAGE = auto()  # 图像类型

class Content:  # 定义 Content 类
    def __init__(self, content_type, original, translation=None):  # 初始化函数，传入内容类型、原始内容和翻译内容（可选）
        self.content_type = content_type  # 将内容类型存储到实例变量中
        self.original = original  # 将原始内容存储到实例变量中
        self.translation = translation  # 将翻译内容存储到实例变量中
        self.status = False  # 初始化翻译状态为 False

    def set_translation(self, translation, status):  # 设置翻译内容和翻译状态的方法，传入翻译内容和翻译状态
        if not self.check_translation_type(translation):  # 如果翻译内容类型不符合要求
            raise ValueError(f"Invalid translation type. Expected {self.content_type}, but got {type(translation)}")  # 抛出 ValueError 异常
        self.translation = translation  # 将翻译内容存储到实例变量中
        self.status = status  # 将翻译状态存储到实例变量中

    def check_translation_type(self, translation):  # 检查翻译内容类型的方法，传入翻译内容
        if self.content_type == ContentType.TEXT and isinstance(translation, str):  # 如果内容类型为 TEXT，且翻译内容为字符串类型
            return True  # 返回 True
        elif self.content_type == ContentType.TABLE and isinstance(translation, list):  # 如果内容类型为 TABLE，且翻译内容为列表类型
            return True  # 返回 True
        elif self.content_type == ContentType.IMAGE and isinstance(translation, PILImage.Image):  # 如果内容类型为 IMAGE，且翻译内容为 PIL 库中的 Image 类型
            return True  # 返回 True
        return False  # 否则返回 False

    def __str__(self):  # 定义 __str__ 方法，返回原始内容
        return self.original


class TableContent(Content):  # 定义 TableContent 类，继承自 Content 类
    def __init__(self, data, translation=None):  # 初始化函数，传入表格数据和翻译内容（可选）
        df = pd.DataFrame(data)  # 将表格数据转换为 DataFrame 对象

        # 验证提取的表格数据和 DataFrame 对象的行数和列数是否匹配
        if len(data) != len(df) or len(data[0]) != len(df.columns):
            raise ValueError("The number of rows and columns in the extracted table data and DataFrame object do not match.")
        
        super().__init__(ContentType.TABLE, df)  # 调用父类的初始化函数，传入内容类型和 DataFrame 对象

    def set_translation(self, translation, status):  # 设置翻译内容和翻译状态的方法，传入翻译内容和翻译状态
        try:
            if not isinstance(translation, str):  # 如果翻译内容不是字符串类型
                raise ValueError(f"Invalid translation type. Expected str, but got {type(translation)}")  # 抛出 ValueError 异常

            LOG.debug(f"[translation]\n{translation}")  # 输出调试信息
            # 从第一组方括号中提取列名
            header = translation.split(']')[0][1:].split(', ')
            # 从剩余的方括号中提取数据行
            data_rows = translation.split('] ')[1:]
            # 将数据行中的每一行转换为列表
            data_rows = [row[1:-1].split(', ') for row in data_rows]
            # 使用提取的列名和数据创建 DataFrame
            translated_df = pd.DataFrame(data_rows, columns=header)
            LOG.debug(f"[translated_df]\n{translated_df}")
            self.translation = translated_df  # 将翻译后的 DataFrame 存储到实例变量中
            self.status = status  # 将翻译状态存储到实例变量中
        except Exception as e:  # 捕获所有异常
            LOG.error(f"An error occurred during table translation: {e}")  # 输出错误信息
            self.translation = None  # 将翻译内容设置为 None
            self.status = False  # 将翻译状态设置为 False

    def __str__(self):  # 定义 __str__ 方法，返回原始内容的字符串表示（不包括表头和行号）
        return self.original.to_string(header=False, index=False)

    def iter_items(self, translated=False):  # 定义迭代表格元素的方法，传入是否翻译的标志
        target_df = self.translation if translated else self.original  # 根据是否翻译的标志选择要迭代的 DataFrame
        for row_idx, row in target_df.iterrows():  # 遍历 DataFrame 的每一行
            for col_idx, item in enumerate(row):  # 遍历每一行的每一列
                yield (row_idx, col_idx, item)  # 返回行索引、列索引和元素值的元组

    def update_item(self, row_idx, col_idx, new_value, translated=False):  # 定义更新表格元素的方法，传入行索引、列索引、新值和是否翻译的标志
        target_df = self.translation if translated else self.original  # 根据是否翻译的标志选择要更新的 DataFrame
        target_df.at[row_idx, col_idx] = new_value  # 更新指定位置的元素值

    def get_original_as_str(self):  # 定义获取原始内容的字符串表示的方法
        return self.original.to_string(header=False, index=False)