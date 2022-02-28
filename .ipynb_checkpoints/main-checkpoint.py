import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interation{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

# チェックボックスの作成
# if st.checkbox('Show Image'):
#     img = Image.open('test.png')
#     st.image(img, caption='test', use_column_width=True)

# セレクトボックスの作成
# option = st.selectbox(
#     'あなたが好きな数字は？' , 
#     list(range(1, 11))
# )

# 'あなたの好きな数字は？', option, 'です'

left_column, right_column = st.columns(2)
button = left_column.button('右からカラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

    
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容')

# テキスト入力
# text = st.text_input('あなたの趣味は？')
# スライダー
# condition = st.slider('あなたの今の調子は', 0, 100, 50)

# 'あなたの趣味は', text, 'です'
# 'あなたの調子は', condition, 'です'


# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns =['lat','lon']
# )

# st.write(df)   writeには引数なし
# st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
# st.table(df.style.highlight_max(axis=0))   # staticな表を作る場合


# 折れ線グラフを各
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# st.map(df)

"""
# 小
## 節
### 項

コードの書き方
```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""
