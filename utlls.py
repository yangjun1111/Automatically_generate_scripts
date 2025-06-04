from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from langchain_core.messages import SystemMessage, HumanMessage

def generate_script(subject,video_length,creativity,api_key):
    
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human","请为'{subject}'生成一个标题，标题需要简洁明了，能够吸引观众，并且符合youtube的SEO标准，标题长度在50个字符以内")
        ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位短视频频道的博主。根据以下标题和相关信息，为短视频频道写一个视频脚本。
             视频标题：{title}，视频时长：{duration}分钟，生成的脚本的长度尽量遵循视频时长的要求。
             要求开头抓住限球，中间提供干货内容，结尾有惊喜，脚本格式也请按照【开头、中间，结尾】分隔。
             整体内容的表达方式要尽量轻松有趣，吸引年轻人。
             :
             ```{wikipedia_search}```""")
        ]
    )
    
    model = ChatOpenAI(temperature=creativity,
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # 读取环境变量
    base_url="https://api.deepseek.com",
)
    title_chain = title_template | model
    script_chain = script_template | model

    title = title_chain.invoke({"subject": subject}).content

    # 实际调用 script_chain，传入需要的参数
    script = script_chain.invoke({
        "title": title,
        "duration": video_length,
        "wikipedia_search": ""  # 这里可以根据需要传递实际内容
    }).content

    return script

# print(generate_script("sora模型", 1, 0.7, os.getenv("DEEPSEEK_API_KEY")))