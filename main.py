import base64
from io import BytesIO

import streamlit as st

from get_input import generate_word_image


def get_image_download_link(img,filename,text):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href


## Original image came from cv2 format, fromarray convert into PIL format


st.markdown("""
    ## Conversor de texto para Libras
    
    Ola! Para usar o conversor, basta digitar sua palavra e apertar Enter!
    
    Voce pode criar palavras subsequentes reescrevendo o texto e apertando Enter novamente!
    
    Por enquanto ainda nao eh possivel converter numeros nem identificar espacos!
""")
st.text("")
st.text("")


user_input = st.text_input("Digite a palavra que voce quer converter para LIBRAS: ")

if user_input:
    # st.text(user_input)
    generated_word = generate_word_image(user_input)

    st.image(generated_word)

    st.markdown(
        get_image_download_link(
            generated_word,
            f'{user_input}.png',
            'Clique aqui para baixar o texto gerado: ' + user_input + '.png'
        ), unsafe_allow_html=True)


st.text("")
st.markdown("""
    Feito por arthurtuio com carinho para seu amor <3
""")