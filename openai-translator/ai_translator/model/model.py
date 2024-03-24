from ai_translator.book import ContentType


class Model:
    def make_text_prompt(self, text: str, target_language: str) -> str:
        return f"翻译为{target_language}，保留原文间距（空格，分隔符，换行符）：{text}"

    def make_table_prompt(self, table: str, target_language: str) -> str:
        return f"表格形式：" + \
               "[Fruit, Color, Price (USD)]\n" + \
               "[Apple, Red, 1.20]\n" + \
               f"请将下列文字翻译为{target_language}，保持间距（空格，分隔符），不同行要换行，并以上述表格形式返回：{table}"

    def translate_prompt(self, content, target_language: str) -> str:
        if content.content_type == ContentType.TEXT:
            return self.make_text_prompt(content.original, target_language)
        elif content.content_type == ContentType.TABLE:
            return self.make_table_prompt(content.get_original_as_str(), target_language)

    def make_request(self, prompt):
        raise NotImplementedError("子类必须实现 make_request 方法")
