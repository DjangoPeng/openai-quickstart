"""
相关数据类型的定义
"""
from typing import Literal, TypedDict, List, Union, Optional, TYPE_CHECKING
if TYPE_CHECKING:
    import streamlit.elements.image

class BaseMsg(TypedDict):
    pass


class TextMsg(BaseMsg):
    """文本消息"""
    
    # 在类属性标注的下一行用三引号注释，vscode中
    role: Literal["user", "assistant"]
    """消息来源"""
    content: str
    """消息内容"""


class ImageMsg(BaseMsg):
    """图片消息"""
    role: Literal["image"]
    image: "streamlit.elements.image.ImageOrImageList"
    """图片内容"""
    caption: Optional[Union[str, List[str]]]
    """说明文字"""


Msg = Union[TextMsg, ImageMsg]
TextMsgList = List[TextMsg]
MsgList = List[Msg]


class CharacterMeta(TypedDict):
    """角色扮演设定，它是CharacterGLM API所需的参数"""
    user_info: str
    """用户人设"""
    bot_info: str
    """角色人设"""
    bot_name: str
    """bot扮演的角色的名字"""
    user_name: str
    """用户的名字"""


def filter_text_msg(messages: MsgList) -> TextMsgList:
    return [m for m in messages if m["role"] != "image"]


if __name__ == "__main__":
    # 尝试在VSCode等IDE中自己敲一遍下面的代码，观察IDE能提供哪些代码提示
    text_msg = TextMsg(role="user")
    text_msg["content"] = "42"
    print(type(text_msg))
    print(text_msg)
