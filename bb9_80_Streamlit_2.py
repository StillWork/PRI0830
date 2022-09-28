# streamlit 설치       pip install streamlit
# 실행 방법 (명령창에서)   streamlit run d_80_Streamlit.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff


st.title('타이틀입니다')
st.header("제목")
st.subheader("소제목")
st.write("임의의 내용을 입력합니다.")

if st.button("Button"):
    st.write("버튼을 눌렀습니다.")
    # 임의의 작업 수행 코드
    
if st.checkbox('Checktbox'):
    st.write('선택!')
    
st.header("데이터프레임 보기")

# st.dataframe을 사용하면 인터랙티브한 테이블을 볼 수 있고
# st.table을 사용하면 정적인 테이블을 볼 수 있음

# 데이터프레임 샘플
df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.subheader("소팅이 가능한 데이터프레임(컬럼 클릭)")
st.dataframe(df)

st.subheader("정적인 테이블")
st.table(df)

# 그래프 그리기
st.header("데이터프레임 그래프")

st.subheader("line_chart")
st.line_chart(df)

st.subheader("area_chart")
st.area_chart(df)

st.subheader("bar_chart")
st.bar_chart(df)

st.subheader("pyplot")

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

st.subheader("plotly_chart")

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]
group_labels = ["Group 1", "Group 2", "Group 3"]

fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])
st.plotly_chart(fig)

st.subheader("vega_lite_chart")

df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

st.vega_lite_chart(df,
    {
        "mark": {"type": "circle", "tooltip": True},
        "encoding": {
            "x": {"field": "a", "type": "quantitative"},
            "y": {"field": "b", "type": "quantitative"},
            "size": {"field": "c", "type": "quantitative"},
            "color": {"field": "c", "type": "quantitative"},
        },
    },
    use_container_width=True,
)

st.header("레이아웃(홈페이지 처럼)")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

with col2:
   st.header("Button")
   if st.button("Button!!"):
           st.write("버튼......")

with col3:
	st.header("Chart Data")
	chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
	st.bar_chart(chart_data)
    
value = st.text_input("변수 갯수 입력하세요 i: ")

# 키 입력 받기
if value:
    st.write("이 변수를 사용합니다, i = ", value)
    # Some code
