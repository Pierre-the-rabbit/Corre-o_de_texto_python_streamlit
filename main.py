

#Criação de um site capaz de realizar correções textuais:

#Imports
import streamlit as st 
import language_tool_python

#as variaveis
place_h = "texti"

#Titulo
st.title("Correção de texto")

#determinar as colunas
col1, col2 = st.columns(2, border=True)

#coluna 1
with col1:
    #inserir o texto a ser corrigido
    st.subheader("Texto original:")
    texto = st.text_area("Digite seu texto...")


#função para corrigir o texto
def Correcao_do_texto():
    #criação das variaveis
    tool = language_tool_python.LanguageTool("pt-BR")
    correcao = tool.correct(texto)
    erros = tool.check(texto)
    #criação da coluna 2
    with col2:
        st.subheader("Texto com correção:")
        texto_corrigido = st.text_area(" ",f"{correcao}", disabled=False)

    #sidebar    
    st.sidebar.subheader("Correções realizadas no texto")

    #encontra erros e coloca na sidebar
    if erros:
        st.sidebar.write(f"Foram encontrados {len(erros)} falha(s)")
        st.sidebar.divider()
        ordem = 1
        for match in erros:
            
            st.sidebar.subheader(f"N {ordem}° Error: {match.message}")
            st.sidebar.write(f"Sugestões de correção: {match.replacements}")
            st.sidebar.write(f"Regra: {match.ruleId}")
            st.sidebar.divider()
            ordem += 1
            
    else:
        st.sidebar.write("Não foram encontrados falhas")
        
#botão
botao = st.button(label="Vamos corrigri!", on_click=Correcao_do_texto())

