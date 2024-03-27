## 需求：
1. 支持图形用户界面（GUI），提升易用性。
2. 添加对保留源 PDF 的原始布局的支持。
3. 服务化：以 API 形式提供翻译服务支持。
4. 添加对其他语言的支持。

---

## 解决方案:
1. TBD: 采用VUE书写前端页面，提供提交文件、输入文字、提交按钮、展示翻译结果、选择翻译语言项的内容块
2. DONE: 采用flask，将服务调整为接口的模式，对前端提供服务
3. DONE:接口支持提供其他语言的翻译选项，language=English，默认为中文。


## 测试:
```shell
# 需按情况调整文件路径
curl --location --request POST 'http://localhost:5000/translate' \
--form 'file=@".openai-translator_v2.0/tests/test.pdf"' \
--form 'language="中文"'
```