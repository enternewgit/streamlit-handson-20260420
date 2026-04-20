import streamlit as st

st.title("はじめてのStreamlit")
st.write("hello world")
st.write("Streamlitは、Pythonで簡単にWebアプリを作成できるフレームワークです。")
name = st.text_input("名前を入力してね")
if st.button("送信"):
    st.write(f"{name}さん、こんにちは！")