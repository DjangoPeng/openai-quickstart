import time
from dotenv import load_dotenv
load_dotenv()

from api import get_characterglm_response


def characterglm_example():
    character_meta = {
        "user_info": "",
        "bot_info": "小白，性别女，17岁，平溪孤儿院的孩子。小白患有先天的白血病，头发为银白色。小白身高158cm，体重43kg。小白的名字是孤儿院院长给起的名字，因为小白是在漫天大雪白茫茫的一片土地上被捡到的。小白经常穿一身破旧的红裙子，只是为了让自己的气色看上去红润一些。小白初中毕业，没有上高中，学历水平比较低。小白在孤儿院相处最好的一个人是阿南，小白喊阿南哥哥。阿南对小白很好。",
        "user_name": "用户",
        "bot_name": "小白"
    }
    messages = [
        {"role": "assistant", "content": "哥哥，我会死吗？"},
        {"role": "user", "content": "（微信）怎么会呢？医生说你的病情已经好转了"}
    ]
    for chunk in get_characterglm_response(messages, meta=character_meta):
        print(chunk)
        time.sleep(0.5)


if __name__ == "__main__":
    characterglm_example()
