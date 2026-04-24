import streamlit as st

def main():
    st.set_page_config(
        page_title='Aplicativos - SRAS',
        page_icon='🕮',
        layout='wide')   
    
    with open('configApps.css') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)   
    
    buttUrls = [['Formulário TJMA', 
                 'https://formreport-rmtbndsjrmydcvhz5jxpcp.streamlit.app/', 
                 ':material/assignment_add:'], 
                ['Calculadora de datas', 
                 'https://calculodatas-bbpyhvlpqtc39cwtvznt9r.streamlit.app/', 
                 ':material/calendar_month:'], 
                ['PDF plus', 
                 'https://toolsforpdfs-ykileuue4fcthdkq4sarmo.streamlit.app/', 
                 ':material/magnify_docked:'], 
                ['Conversor de Tabelas', 
                 'https://filesconvertallformats-f6smdezskexpltbrcqbtmz.streamlit.app/', 
                 ':material/table_convert:'], 
                ['Conversor de texto', 
                 'https://alltexts-lpgaq6mkqcuc6xthctrg8s.streamlit.app/', 
                 ':material/text_snippet:'], 
                ['Visualizador de imagens', 
                 'https://viewerpdf-o9cboaczuavjfj2ptfn3f3.streamlit.app/', 
                 ':material/image:']
                ]
    st.subheader('Galeria de aplicativos')

    col1, col2, col3 = st.columns(spec=3)
    col1.link_button(label=buttUrls[0][0], url=buttUrls[0][1], 
                     use_container_width=True, width="stretch", icon=buttUrls[0][2])
    col2.link_button(label=buttUrls[1][0], url=buttUrls[1][1], 
                     use_container_width=True, width="stretch", icon=buttUrls[1][2])
    col3.link_button(label=buttUrls[2][0], url=buttUrls[2][1], 
                     use_container_width=True, width="stretch", icon=buttUrls[2][2])
    
    col4, col5, col6 = st.columns(spec=3)
    col4.link_button(label=buttUrls[3][0], url=buttUrls[3][1], 
                     use_container_width=True, width="stretch", icon=buttUrls[3][2])
    col5.link_button(label=buttUrls[4][0], url=buttUrls[4][1], 
                     use_container_width=True, width="stretch", icon=buttUrls[4][2])
    col6.link_button(label=buttUrls[5][0], url=buttUrls[5][1], 
                     use_container_width=True, width="stretch", icon=buttUrls[5][2])
    
    

if __name__ == '__main__':  
    main()
