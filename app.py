import streamlit as st
from PIL import Image
from PIL.ImageFilter import *
st.markdown("<h1 style='text-align:center;'>Image Editor</h1>",unsafe_allow_html=True)
st.markdown("---")
image=st.file_uploader("Upload Image",type=["jpg","png","jpeg"])
st.image(image)
size=st.empty()#it is empty place holder 
mode=st.empty()#it is empty place holder 
format_=st.empty()#it is empty place holder 
if image:
    img=Image.open(image)#here we used pillow library to extract the image information
    size.markdown(f"<h6>Size :{img.size}</h6>",unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode :{img.mode}</h6>",unsafe_allow_html=True)
    format_.markdown(f"<h6>Size :{img.format}</h6>",unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Resize</h2>",unsafe_allow_html=True)
    width=st.number_input("Width",value=img.width)
    hieght=st.number_input("Hiegh",value=img.height)
    st.markdown("<h2 style='text-align:center;'>Rotation</h2>",unsafe_allow_html=True)
    Degree=st.number_input("Degree")
    st.markdown("<h2 style='text-align:center;'>Filter</h2>",unsafe_allow_html=True)
    filters=st.selectbox("Filters",options=["None","BLUR","CONTOUR","DETAIL","EMBOSS","SMOOTH"])
    st_btn=st.button("Submit")
    if st_btn:
        edited=img.resize((width,hieght)).rotate(Degree)
        if filters!="None":
            if filters=="BLUR":
                edited=edited.filter(BLUR)
            elif filters=="CONTOUR":
                edited=edited.filter(CONTOUR)
            elif filters=="DETAIL":
                edited=edited.filter(DETAIL)
            elif filters=="EMBOSS":
                edited=edited.filter(EMBOSS)
            elif filters=="SMOOTH":
                edited=edited.filter(SMOOTH)
          
        st.image(edited)