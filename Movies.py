import streamlit as st
import pickle


import streamlit as st
import base64

# def add_local_background(image_path):
#     with open(image_path, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url(data:image/jpeg;base64,{encoded_string});
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# Provide the path to your local image
# add_local_background('netflix_movies_cover.jpg')




final_df = pickle.load(open('final_df.pkl','rb'))
sim = pickle.load(open('sim.pkl','rb'))
st.title('Movies Recommendation')
movi = st.selectbox('**Movie**',options=final_df['title'])

btn = st.button('Recommend')
def recommend(movi):
        ind = final_df[final_df['title']==movi].index[0]
        rec_mov_int = sorted(enumerate(sim[ind]),key=lambda x:x[1],reverse=True)[1:6]
        temp = []
        rec_fin = []
        for i in rec_mov_int:
            temp.append(i[0])

        rec_fin.append(final_df['title'].iloc[temp])
        for i in rec_fin[0].values:
            st.write(i)
if btn:
    recommend(movi)
    