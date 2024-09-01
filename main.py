import streamlit as st

from get_input import generate_word_image


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
    st.image(generate_word_image(user_input))


st.text("")
st.markdown("""
    Feito por arthurtuio com carinho para seu amor <3
""")