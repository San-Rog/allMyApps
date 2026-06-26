import streamlit as st

def main():
    st.set_page_config(
        page_title='Aplicativos - SRAS',
        page_icon='🕮',
        layout='wide')   
    
    with open(r'C:\Users\ACER\Documents\css\configApps.css') as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)   
    
    buttUrls = [['Conversor de imagens', 
                 'https://convertallimagetoimage-pn9uhxmd5nqmwcytmiossr.streamlit.app/', 
                 ':material/reset_image:'], 
                ['Mescla de imagens', 
                 'https://imagetopdftodocx-ny7max5gwznawux9jcrjr8.streamlit.app/', 
                 ':material/join_right:'], 
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
                 ':material/image:'], 
                ['Formulário TJMA', 
                 'https://formreport-rmtbndsjrmydcvhz5jxpcp.streamlit.app/', 
                 ':material/contract:']
                ]
    st.subheader('Galeria de aplicativos')
    nCols = int(len(buttUrls)/2)
    colsOne = st.columns(spec=nCols)
    colsTwo = st.columns(spec=nCols)
    colsAll = [colsOne, colsTwo]
    for cl, cols in enumerate(colsAll): 
        plus = 0 if cl == 0 else nCols
        for c, col in enumerate(cols):
            c += plus
            col.link_button(label=buttUrls[c][0], url=buttUrls[c][1], 
                            use_container_width=True, width="stretch", icon=buttUrls[c][2])
            
if __name__ == '__main__':  
    main()
