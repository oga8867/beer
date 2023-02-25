import pandas as pd
import streamlit as st
a = pd.read_csv('/app/beer/beer_profile_and_ratings.csv')
a = pd.DataFrame(a.iloc[:,[1,3,5,6,7,-3]])
# 1스타일, 3맥주이름, 5ABV, 6minIBU,7MaxIBU


st.title('welcome to my beer recommander')

#streamlit run main.py

IBU = st.slider('IBU',0.0, 100.0,(0.0))
ABV_se = st.slider('ABV',0.0,15.0,(0.0))
recommand = st.button('맥주 좋아하는 곰의 맥주 킁킁!')




if recommand:


    b = a[a['Max IBU']<=IBU+10]
    b = b[b['Max IBU']>=IBU]
    b = b[b['ABV']>=ABV_se-1]
    b = b[b['ABV']<=ABV_se+1]

    b = b[0:3]

    name = b.values.tolist()
    if len(name) ==0:
        b = a[a['Max IBU'] <= IBU + 10]
        b = b[b['Max IBU'] >= IBU]
        b = b[0:3]
        name = b.values.tolist()
        st.write('추천 맥주가 없네요, 혹시 이런건 어떠세요?')
        st.write(f'{name[0][0]} 스타일의, {name[0][1]} 맥주입니다! ')
    else:
        st.write(f'당신의 추천맥주의 스타일은 {name[0][0]} 입니다. ')
        st.write(f'그리고 맥주 이름은 {name[0][1]}입니다!')

    if len(name) <3:
        st.write('그 외 추천 맥주가 많이 없습니다.')
    else:
        st.write(f'그외의 추천 맥주으로는 {name[1][0]}의 스타일을 가진, {name[1][1]}가 있습니다.')
        st.write(f'또한 다른 추천으로는 {name[2][0]}의 스타일을 가진, {name[2][1]}가 있습니다.')
