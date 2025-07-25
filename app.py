import streamlit as st

# 初期化
if 'names' not in st.session_state:
    st.session_state.names = []

st.title("👤 名前ブロックツール")

# 入力欄
name = st.text_input("名前を入力")
if st.button("追加") and name:
    st.session_state.names.append(name)
    st.rerun()

# 表示
st.subheader("🧱 名前リスト")

# 削除対象のインデックスを記録
delete_index = None

for i, n in enumerate(st.session_state.names):
    col1, col2 = st.columns([4, 1])
    col1.write(f"{i+1}. {n}")
    if col2.button("削除", key=f"delete_{i}"):
        delete_index = i

# 削除処理（ループ後に実行）
if delete_index is not None:
    st.session_state.names.pop(delete_index)
    st.rerun()
