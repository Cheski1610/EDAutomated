import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.image('Logo_Inicial.jpg', use_column_width=True)

st.markdown("<h1 style='text-align: center; color:#4682B4; '>Análisis Exploratorio de Datos Automatizado</h1>", unsafe_allow_html=True)

st.sidebar.image('Logo_sidebar.jpg', width=286)

st.sidebar.info('Esta app fue creada para generar un análisis exploratorio de los datos de manera automática.')

add_selectbox = st.sidebar.selectbox(
"Formato del Archivo",
("XLSX", "CSV"))

if add_selectbox == 'XLSX':
    file_upload = st.file_uploader(":orange[Carga el archivo para análisis]", type=["xlsx"])

    if file_upload is not None:
        data = pd.read_excel(file_upload)
            
        st.header(':red[Análisis Descriptivo]')

        raws_1 = st.number_input('Número de Filas', min_value=0, max_value=50, value=5)
        st.subheader(f'Primeras {raws_1} líneas', divider='blue')
        st.write(data.head(raws_1))

        st.subheader(f'Últimas {raws_1} líneas', divider='blue')
        st.write(data.tail(raws_1))

        st.subheader('Dimensiones de la base de datos', divider='blue')
        st.write(f'Número de filas: {data.shape[0]}')
        st.write(f'Número de columnas: {data.shape[1]}')

        st.subheader('Descripción estadística', divider='blue')
        st.write(data.describe().T)

        st.subheader('Tipos de Datos', divider='blue')
        st.write(pd.DataFrame(data=data.dtypes, columns=['Tipo']))

        st.subheader('Cantidad de Variables', divider='blue')
        st.write(f"Variables cualitativas: {data.select_dtypes(include='object').shape[1]}")
        st.write(f"Variables cuantitativas: {data.select_dtypes(exclude='object').shape[1]}")

        st.subheader('Valores Faltantes', divider='blue')
        st.write(pd.DataFrame(data=data.isnull().sum().sort_values(ascending=False), columns=['Cantidad']))

        st.subheader('Valores Duplicados', divider='blue')
        st.write(data.duplicated().sum())
        st.write(data[data.duplicated()])

        st.subheader('Distribución de las Variables Cuantitativas', divider='blue')
        column = st.selectbox('Variable', data.select_dtypes(exclude='object').columns)
        fig_1, ax = plt.subplots()
        sns.histplot(data[column], bins='auto', kde=True)
        st.pyplot(fig_1)
        column_3 = st.selectbox('Selecc. Variable Cualitativa', data.select_dtypes(include='object').columns)
        fig_6, ax = plt.subplots()
        sns.barplot(data=data, x=column_3, y=column, estimator='sum', errorbar=None)
        ax.set_title('Total por Variable Categórica')
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{height:,.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 6), textcoords='offset points')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig_6)

        st.subheader('Composición de las Variables Cualitativas', divider='blue')
        column_1 = st.selectbox('Variable', data.select_dtypes(include='object').columns)
        fig_3 = px.histogram(data, x=column_1, nbins=10, text_auto=True)
        st.plotly_chart(fig_3)

        st.subheader('Correlación de las Variables', divider='blue')
        corr = data.select_dtypes(exclude='object').corr().round(2)
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="crest", ax=ax)
        st.pyplot(fig)

        st.subheader('Relación entre Variables Cuantitativas', divider='blue')
        column_A = st.selectbox('Variable A', data.select_dtypes(exclude='object').columns)
        column_B = st.selectbox('Variable B', data.select_dtypes(exclude='object').columns)
        fig_4 = px.scatter(data, x=column_A, y=column_B)
        st.plotly_chart(fig_4)

        st.subheader('Promedio por Variable Cualitativa', divider='blue')
        column_1 = st.selectbox('Variable Cualitativa', data.select_dtypes(include='object').columns)
        column_2 = st.selectbox('Variable Cuantitativa', data.select_dtypes(exclude='object').columns)
        fig_5, ax = plt.subplots()
        sns.barplot(data=data, x=column_1, y=column_2, estimator='mean', errorbar=None)
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{height:,.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 6), textcoords='offset points')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig_5)

        st.subheader('Identificación de Valores Atípicos', divider='blue')
        column_A = st.selectbox('Variable de Interés', data.select_dtypes(exclude='object').columns)
        fig_7= px.box(data, y=column_A)
        st.plotly_chart(fig_7)


if add_selectbox == 'CSV':
    file_upload = st.file_uploader(":orange[Carga el archivo para análisis]", type=["csv"])
    
    if file_upload is not None:
        data = pd.read_csv(file_upload)

        st.header(':red[Análisis Descriptivo]')

        raws_1 = st.number_input('Número de Filas', min_value=0, max_value=50, value=5)
        st.subheader(f'Primeras {raws_1} líneas', divider='blue')
        st.write(data.head(raws_1))

        st.subheader(f'Últimas {raws_1} líneas', divider='blue')
        st.write(data.tail(raws_1))

        st.subheader('Dimensiones de la base de datos', divider='blue')
        st.write(f'Número de filas: {data.shape[0]}')
        st.write(f'Número de columnas: {data.shape[1]}')

        st.subheader('Descripción estadística', divider='blue')
        st.write(data.describe().T)

        st.subheader('Tipos de Datos', divider='blue')
        st.write(pd.DataFrame(data=data.dtypes, columns=['Tipo']))

        st.subheader('Cantidad de Variables', divider='blue')
        st.write(f"Variables cualitativas: {data.select_dtypes(include='object').shape[1]}")
        st.write(f"Variables cuantitativas: {data.select_dtypes(exclude='object').shape[1]}")

        st.subheader('Valores Faltantes', divider='blue')
        st.write(pd.DataFrame(data=data.isnull().sum().sort_values(ascending=False), columns=['Cantidad']))

        st.subheader('Valores Duplicados', divider='blue')
        st.write(data.duplicated().sum())
        st.write(data[data.duplicated()])

        st.subheader('Distribución de las Variables Cuantitativas', divider='blue')
        column = st.selectbox('Variable', data.select_dtypes(exclude='object').columns)
        fig_1, ax = plt.subplots()
        sns.histplot(data[column], bins='auto', kde=True)
        st.pyplot(fig_1)
        column_3 = st.selectbox('Selecc. Variable Cualitativa', data.select_dtypes(include='object').columns)
        fig_6, ax = plt.subplots()
        sns.barplot(data=data, x=column_3, y=column, estimator='sum', errorbar=None)
        ax.set_title('Total por Variable Categórica')
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{height:,.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 6), textcoords='offset points')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig_6)

        st.subheader('Composición de las Variables Cualitativas', divider='blue')
        column_1 = st.selectbox('Variable', data.select_dtypes(include='object').columns)
        fig_3 = px.histogram(data, x=column_1, nbins=10, text_auto=True)
        st.plotly_chart(fig_3)

        st.subheader('Correlación de las Variables', divider='blue')
        corr = data.select_dtypes(exclude='object').corr().round(2)
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="crest", ax=ax)
        st.pyplot(fig)

        st.subheader('Relación entre Variables Cuantitativas', divider='blue')
        column_A = st.selectbox('Variable A', data.select_dtypes(exclude='object').columns)
        column_B = st.selectbox('Variable B', data.select_dtypes(exclude='object').columns)
        fig_4 = px.scatter(data, x=column_A, y=column_B)
        st.plotly_chart(fig_4)

        st.subheader('Promedio por Variable Cualitativa', divider='blue')
        column_1 = st.selectbox('Variable Cualitativa', data.select_dtypes(include='object').columns)
        column_2 = st.selectbox('Variable Cuantitativa', data.select_dtypes(exclude='object').columns)
        fig_5, ax = plt.subplots()
        sns.barplot(data=data, x=column_1, y=column_2, estimator='mean', errorbar=None)
        for p in ax.patches:
            height = p.get_height()
            ax.annotate(f'{height:,.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 6), textcoords='offset points')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig_5)

        st.subheader('Identificación de Valores Atípicos', divider='blue')
        column_A = st.selectbox('Variable de Interés', data.select_dtypes(exclude='object').columns)
        fig_7= px.box(data, y=column_A)
        st.plotly_chart(fig_7)

st.text_input(':blue[CONCLUSIONES]', '')

st.caption(':orange[Elaborado por Auditoría Interna]')