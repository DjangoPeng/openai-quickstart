# 导入 pandas 库，用于数据处理
import pandas as pd
# 导入 Enum 和 auto，用于创建枚举类型
from enum import Enum, auto
# 导入 PIL 库中的 Image 类，用于图像处理
from PIL import Image as PILImage
# 导入自定义的 LOG 函数，用于日志记录
from utils import LOG

# 定义 ContentType 枚举类，包含 TEXT、TABLE 和 IMAGE 三种类型
class ContentType(Enum):
    TEXT = auto()
    TABLE = auto()
    IMAGE = auto()

# 定义 Content 类，包含 content_type、original、translation 和 status 四个属性
class Content:
    def __init__(self, content_type, original, translation=None):
        self.content_type = content_type  # 内容类型
        self.original = original  # 原始内容
        self.translation = translation  # 翻译后的内容
        self.status = False  # 翻译状态，默认为 False

    # 设置翻译后的内容和翻译状态
    def set_translation(self, translation, status):
        # 检查翻译类型是否正确
        if not self.check_translation_type(translation):
            raise ValueError(f"Invalid translation type. Expected {self.content_type}, but got {type(translation)}")
        self.translation = translation
        self.status = status

    # 检查翻译类型是否正确
    def check_translation_type(self, translation):
        if self.content_type == ContentType.TEXT and isinstance(translation, str):
            return True
        elif self.content_type == ContentType.TABLE and isinstance(translation, list):
            return True
        elif self.content_type == ContentType.IMAGE and isinstance(translation, PILImage.Image):
            return True
        return False

# 定义 TableContent 类，继承自 Content 类
class TableContent(Content):
    def __init__(self, data, translation=None):
        df = pd.DataFrame(data)

        # 验证提取的表格数据和 DataFrame 对象的行数和列数是否匹配
        if len(data) != len(df) or len(data[0]) != len(df.columns):
            raise ValueError("The number of rows and columns in the extracted table data and DataFrame object do not match.")
        
        # 调用父类的构造函数，设置内容类型为表格，内容为 DataFrame 对象
        super().__init__(ContentType.TABLE, df)

    # 设置翻译后的内容和翻译状态
    def set_translation(self, translation, status):
        try:
            # 如果翻译不是字符串类型，则抛出异常
            if not isinstance(translation, str):
                raise ValueError(f"Invalid translation type. Expected str, but got {type(translation)}")

            LOG.debug(translation)
            # 将字符串转换为列表形式
            table_data = [row.strip().split() for row in translation.strip().split('\n')]
            LOG.debug(table_data)
            # 从 table_data 创建 DataFrame
            translated_df = pd.DataFrame(table_data[1:], columns=table_data[0])
            LOG.debug(translated_df)
            self.translation = translated_df
            self.status = status
        except Exception as e:
            LOG.error(f"An error occurred during table translation: {e}")
            self.translation = None
            self.status = False

    # 将 DataFrame 转换为字符串形式
    def __str__(self):
        return self.original.to_string(header=False, index=False)

    # 迭代表格中的每个元素
    def iter_items(self, translated=False):
        target_df = self.translation if translated else self.original
        for row_idx, row in target_df.iterrows():
            for col_idx, item in enumerate(row):
                yield (row_idx, col_idx, item)

    # 更新表格中的元素
    def update_item(self, row_idx, col_idx, new_value, translated=False):
        target_df = self.translation if translated else self.original
        target_df.at[row_idx, col_idx] = new_value

    # 获取原始表格的字符串形式
    def get_original_as_str(self):
        return self.original.to_string(header=False, index=False)