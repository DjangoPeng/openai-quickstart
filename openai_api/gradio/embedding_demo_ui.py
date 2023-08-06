# 导入 pandas 包。Pandas 是一个用于数据处理和分析的 Python 库
# 提供了 DataFrame 数据结构，方便进行数据的读取、处理、分析等操作。
import pandas as pd
# 导入 tiktoken 库。Tiktoken 是 OpenAI 开发的一个库，用于从模型生成的文本中计算 token 数量。
import tiktoken
# 从 openai.embeddings_utils 包中导入 get_embedding 函数。
# 这个函数可以获取 GPT-3 模型生成的嵌入向量。
# 嵌入向量是模型内部用于表示输入数据的一种形式。
from openai.embeddings_utils import get_embedding
import openai
import gradio as gr
import os
import sys
from tkinter import filedialog, Tk
import ast
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

# 填入自己的apikey
openai.api_key = ''
df = None


def get_any_file_path(file_path=''):
    ENV_EXCLUSION = ['COLAB_GPU', 'RUNPOD_POD_ID']
    if (
            not any(var in os.environ for var in ENV_EXCLUSION)
            and sys.platform != 'darwin'
    ):
        current_file_path = file_path
        initial_dir, initial_file = get_dir_and_file(file_path)

        root = Tk()
        root.wm_attributes('-topmost', 1)
        root.withdraw()
        file_path = filedialog.askopenfilename(
            initialdir=initial_dir,
            initialfile=initial_file,
        )
        root.destroy()

        if file_path == '':
            file_path = current_file_path

    return file_path


def get_dir_and_file(file_path):
    dir_path, file_name = os.path.split(file_path)
    return (dir_path, file_name)


def preview_csv(source_csv):
    global df
    # 加载数据集
    df = pd.read_csv(source_csv, index_col=0)
    if "embedding_vec" in df.columns:
        df = df[["embedding_vec"]]
    elif "embedding" in df.columns:
        df = df[["embedding"]]
    else:
        df = df[["Time", "ProductId", "UserId", "Score", "Summary", "Text"]]
        df = df.dropna()

        if "combined" not in df.columns:
            # 将 "Summary" 和 "Text" 字段组合成新的字段 "combined"
            df["combined"] = (
                    "Title: " + df.Summary.str.strip() + "; Content: " + df.Text.str.strip()
            )

    return df


'''
调用openpi的embedding模型，进行文本分析，并保存结果
'''


def do_embedding(df, api_key, embedding_model, embedding_encoding, max_tokens, top_n):
    openai.api_key = api_key
    df = df.sort_values("Time").tail(top_n * 2)
    # df.drop("Time", axis=1, inplace=True)

    encoding = tiktoken.get_encoding(embedding_encoding)

    # 忽略太长无法嵌入的评论
    df["n_tokens"] = df.combined.apply(lambda x: len(encoding.encode(x)))
    # 删除Token超长的样本
    df = df[df.n_tokens <= max_tokens].tail(top_n)

    # 生成 Embeddings 并保存（非必须步骤，可直接复用项目中文件）
    # 实际生成会耗时几分钟
    # 提醒：非必须步骤，可直接复用项目中的嵌入文件 fine_food_reviews_with_embeddings_1k
    df["embedding"] = df.combined.apply(lambda x: get_embedding(x, engine=embedding_model))
    # 这里可以自定义文件名，注意：第一次跑出来结果后就可以把这三行代码注释掉了，然后以后用这个结果集就行，不然每次都会浪费apikey的token
    embedding_result_output_path = "data/embeddings_demo.csv"
    df.to_csv(embedding_result_output_path)
    return embedding_result_output_path


'''
使用 t-SNE 可视化 Embedding 后的结果
'''


def visual_embedding_result(df_embedded):
    # 首先，确保你的嵌入向量都是等长的
    assert df_embedded['embedding_vec'].apply(len).nunique() == 1

    # 将嵌入向量列表转换为二维 numpy 数组
    matrix = np.vstack(df_embedded['embedding_vec'].values)

    # 创建一个 t-SNE 模型，t-SNE 是一种非线性降维方法，常用于高维数据的可视化。
    # n_components 表示降维后的维度（在这里是2D）
    # perplexity 可以被理解为近邻的数量
    # random_state 是随机数生成器的种子
    # init 设置初始化方式
    # learning_rate 是学习率。
    # tsne = TSNE(n_components=2, perplexity=15, random_state=42, init='random', learning_rate=200)
    # perplexity 需要少于csv文件的列数
    tsne = TSNE(n_components=2, perplexity=15, random_state=42, init='random', learning_rate=200)

    # 使用 t-SNE 对数据进行降维，得到每个数据点在新的2D空间中的坐标
    vis_dims = tsne.fit_transform(matrix)

    # 定义了五种不同的颜色，用于在可视化中表示不同的等级
    colors = ["red", "darkorange", "gold", "turquoise", "darkgreen"]

    # 从降维后的坐标中分别获取所有数据点的横坐标和纵坐标
    x = [x for x, y in vis_dims]
    y = [y for x, y in vis_dims]

    # 根据数据点的评分（减1是因为评分是从1开始的，而颜色索引是从0开始的）获取对应的颜色索引
    color_indices = df_embedded.Score.values - 1

    # 确保你的数据点和颜色索引的数量匹配
    assert len(vis_dims) == len(df_embedded.Score.values)

    # 创建一个基于预定义颜色的颜色映射对象
    colormap = matplotlib.colors.ListedColormap(colors)
    # 使用 matplotlib 创建散点图，其中颜色由颜色映射对象和颜色索引共同决定，alpha 是点的透明度
    plt.scatter(x, y, c=color_indices, cmap=colormap, alpha=0.3)
    # 显示颜色条
    plt.colorbar()

    # 为图形添加标题
    plt.title("评论散点图", fontproperties='Microsoft YaHei')
    comment_visual_img_path = 'images/comment_visual.png'
    plt.savefig(comment_visual_img_path)
    return matrix, comment_visual_img_path


'''
使用 K-Means 聚类，然后使用 t-SNE 可视化 Embedding 后的结果
'''


def cluster_embedding_result(df_embedded, matrix):
    # cluster数要小于等于样本数（csv文件的行数）
    n_clusters = 4

    # 创建一个 KMeans 对象，用于进行 K-Means 聚类。
    # n_clusters 参数指定了要创建的聚类的数量；
    # init 参数指定了初始化方法（在这种情况下是 'k-means++'）；
    # random_state 参数为随机数生成器设定了种子值，用于生成初始聚类中心。
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)

    # 使用 matrix（我们之前创建的矩阵）来训练 KMeans 模型。这将执行 K-Means 聚类算法。
    kmeans.fit(matrix)

    # kmeans.labels_ 属性包含每个输入数据点所属的聚类的索引。
    # 这里，我们创建一个新的 'Cluster' 列，在这个列中，每个数据点都被赋予其所属的聚类的标签。
    df_embedded['Cluster'] = kmeans.labels_

    # 首先为每个聚类定义一个颜色。
    colors = ["red", "green", "blue", "purple"]

    # 然后，你可以使用 t-SNE 来降维数据。这里，我们只考虑 'embedding_vec' 列。
    tsne_model = TSNE(n_components=2, random_state=42)
    vis_data = tsne_model.fit_transform(matrix)

    # 现在，你可以从降维后的数据中获取 x 和 y 坐标。
    x = vis_data[:, 0]
    y = vis_data[:, 1]

    # 'Cluster' 列中的值将被用作颜色索引。
    color_indices = df_embedded['Cluster'].values

    # 创建一个基于预定义颜色的颜色映射对象
    colormap = matplotlib.colors.ListedColormap(colors)

    # 使用 matplotlib 创建散点图，其中颜色由颜色映射对象和颜色索引共同决定
    plt.scatter(x, y, c=color_indices, cmap=colormap)
    # 显示颜色条
    plt.colorbar()

    # 为图形添加标题
    plt.title("评论聚类结果散点图", fontproperties='Microsoft YaHei')
    cluster_visual_img_path = 'images/cluster_result_visual.png'
    plt.savefig(cluster_visual_img_path)
    return cluster_visual_img_path


def handle_embedding(api_key, embedding_model, embedding_encoding, max_tokens, top_n):
    global df
    top_n = int(top_n)
    max_tokens = int(max_tokens)

    # 2.调用openpi的embedding模型，进行文本分析，并保存结果
    embedding_result_output_path = do_embedding(df, api_key, embedding_model, embedding_encoding, max_tokens, top_n)

    df_embedded = pd.read_csv(embedding_result_output_path, index_col=0)
    # 将字符串转换为向量
    df_embedded["embedding_vec"] = df_embedded["embedding"].apply(ast.literal_eval)
    df_embedded.to_csv(embedding_result_output_path)

    # 3. 使用 t-SNE 可视化 Embedding 后的美食评论
    matrix, comment_visual_img_path = visual_embedding_result(df_embedded)

    # 4. 使用 K-Means 聚类，然后使用 t-SNE 可视化
    cluster_visual_img_path = cluster_embedding_result(df_embedded, matrix)

    return embedding_result_output_path, comment_visual_img_path, cluster_visual_img_path


def ui():
    from theme.summer import Summer

    document_symbol = '\U0001F4C4'  # 📄
    css = ''

    # 加载css样式
    if os.path.exists('theme/style.css'):
        with open(os.path.join('theme/style.css'), 'r', encoding='utf8') as file:
            css += file.read() + '\n'

    with gr.Blocks(title="Embedding Study", css=css, theme=Summer()) as interface:
        gr.Markdown('''# <span style='color:brown'>Embedding Study</span> ''')
        api_key = gr.Textbox(label="APIKey", placeholder="请输入API Key")
        with gr.Row():
            source_csv = gr.Textbox(label="数据集", placeholder="请选择 CSV 格式的数据集")
            source_csv_button = gr.Button(value=document_symbol, elem_id='source_csv_button')
            source_csv_button.click(
                get_any_file_path,
                inputs=source_csv,
                outputs=source_csv,
                show_progress=False
            )

        with gr.Row():
            embedding_model = gr.Dropdown(choices=["text-embedding-ada-002"], value="text-embedding-ada-002",
                                          label="Embedding模型")
            embedding_encoding = gr.Dropdown(["cl100k_base"], value="cl100k_base", label="Embedding模型分词器")
        with gr.Row():
            max_tokens = gr.Textbox(label='最大Token', value=8000)
            top_n = gr.Textbox(label='样本数', value=1000)
        with gr.Row():
            go = gr.Button("GO", elem_id='source_csv_button', variant='primary')
        with gr.Row():
            comment_visual_img = gr.Image(label="评论可视化结果")
            comment_cluster_visual_img = gr.Image(label="评论聚类可视化结果")
        with gr.Row():
            csv_output = gr.Dataframe(label="CSV动态读取展示", overflow_row_behaviour='paginate', max_rows=10,
                                      max_cols=4)
        # 监听数据集路径的变化
        source_csv.change(preview_csv, inputs=[source_csv], outputs=csv_output)
        # 绑定点击事件，触发核心逻辑
        go.click(handle_embedding, inputs=[api_key, embedding_model, embedding_encoding, max_tokens, top_n],
                 outputs=[source_csv, comment_visual_img, comment_cluster_visual_img])
        interface.queue(max_size=8).launch()


if __name__ == '__main__':
    ui()
