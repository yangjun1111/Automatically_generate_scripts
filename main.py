import os 
import streamlit as st
from utlls import generate_script

st.title("视频脚本生成器")

with st.sidebar:
    openai_api_key = st.text_input("请输入你的OpenAI API Key", type="password")
    st.markdown("[如何获取OpenAI API Key](https://platform.openai.com/docs/api-reference/introduction)")

subject = st.text_input("💡 输入视频主题")
video_length = st.number_input("🕒 输入视频时长", min_value=1, max_value=10, value=1)
creativity = st.slider("🎨 创造力", min_value=0.0, max_value=1.0, value=0.7)
submit = st.button("🎬 生成脚本")
    # script = generate_script(subject, video_length, creativity, os.getenv("DEEPSEEK_API_KEY"))
if submit and not openai_api_key:
    st.error("请输入你的OpenAI API Key")
    st.stop()
if submit and not subject:
    st.error("请输入你的视频主题")
    st.stop()
if submit and not video_length >= 0.1:
    st.error("视频长度需要大于0.1分钟")
    st.stop()
if submit:
    with st.spinner(("AI正在思考中，请稍等...")):
        script = generate_script(subject, video_length, creativity, openai_api_key)
    st.success("视频脚本已生成！")
    st.subheader("🔥 标题： ")
    st.write(f"**{subject}**")
    st.subheader("视频脚本： ")
    st.write(script)
