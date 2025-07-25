import streamlit as st

# セッション状態で名前リストを保存
if 'names' not in st.session_state:
    st.session_state.names = []

st.title("👤 名前ブロックツール")

# 入力フォーム
name = st.text_input("名前を入力")
if st.button("追加") and name:
    st.session_state.names.append(name)

# 表示
st.subheader("🧱 名前リスト")
for i, n in enumerate(st.session_state.names):
    col1, col2 = st.columns([4, 1])
    col1.write(f"{i+1}. {n}")
    if col2.button("削除", key=i):
        st.session_state.names.pop(i)
        st.experimental_rerun()
