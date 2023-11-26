# 引入 book 中的 ContentType 枚举类型
from book import ContentType

# 定义一个 Model 类
class Model:
    # 定义一个方法，用于生成文本翻译的提示
    def make_text_prompt(self, text: str, target_language: str) -> str:
        # 返回一个字符串，表示将 text 翻译为 target_language
        return f"翻译为{target_language}：{text}"

    # 定义一个方法，用于生成表格翻译的提示
    def make_table_prompt(self, table: str, target_language: str) -> str:
        # 返回一个字符串，表示将 table 翻译为 target_language，并保持原有的间距（空格，分隔符），以表格形式返回
        return f"翻译为{target_language}，保持间距（空格，分隔符），以表格形式返回：\n{table}"

    # 定义一个方法，用于生成翻译提示
    def translate_prompt(self, content, target_language: str) -> str:
        # 判断内容类型，生成相应的翻译提示
        if content.content_type == ContentType.TEXT:
            # 如果内容类型为文本，则调用 make_text_prompt 方法生成翻译提示
            return self.make_text_prompt(content.original, target_language)
        elif content.content_type == ContentType.TABLE:
            # 如果内容类型为表格，则调用 make_table_prompt 方法生成翻译提示
            return self.make_table_prompt(content.get_original_as_str(), target_language)

    # 定义一个方法，用于生成请求
    def make_request(self, prompt):
        # 抛出 NotImplementedError 异常，提示子类必须实现 make_request 方法
        raise NotImplementedError("子类必须实现 make_request 方法")