import streamlit as st

#  text-title

st.title("Streamlit Tutaorials")

#  header-subheader
st.header("This is a header")
st.subheader("This is a subheader")


#  text
st.text("Hello Streamlit")

#  markdown
st.markdown("### This is a markdown")

st.help(st.markdown)

#  Error-Colorfull Text

st.success("Succesful")

st.info("Information")

st.warning("This is a warning")

st.error("This is an error Danger")

st.exception("NameError('name three not defined')")

# Get Help Info About  Python
st.help(range)

# Writing Text
st.write("Text with write")

st.write(range(10))

#images
from PIL import Image
img = Image.open("mypiechart.png")
st.image(img,width = 300, caption = "Simple Image")

#Videos
vid_file=open("VID-20210115-WA0016.mp4", 'rb')
st.video(vid_file)

#audio
audio_file = open("1_1.mp3","rb")
st.audio(audio_file)

#checkbox
if st.checkbox("Show/Hide"):
    st.text("I'm showing because you checked the box")
    
st.checkbox("Hide/Seek")
