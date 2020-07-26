import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import Image
import plotly.express as px

def main():
        """ A simple Analytics App """
        st.header('Sample Analytical App - Guru.K')
        
        #image = Image.open('guru.png')
        #st.image(image, use_column_width=True)
        st.subheader('Charts And Insights')


        st.sidebar.header('Want to know more about data?')
        st.sidebar.text('Yeah, Lets go!')
        st.sidebar.subheader('Overview')
        st.sidebar.markdown('''
        Insights about the given data
        ''')
        
        
        df = pd.read_csv('sitel_csv.csv')
        st.dataframe(df)
        #Trainers Vs Process Complexity (Avg AHT):
        p1= pd.pivot_table(df,values= 'AHT', columns= 'Process Complexity' , index = 'Trainer')
        option1 = st.radio(
             "Type Of Chart",
             ('Bar', 'Line', 'Scatter'))

        if option1 == 'Bar':
            ax = px.bar(p1, x= p1.index, y = ['L1','L2'])
            ax.update_layout(barmode = 'group')
            st.plotly_chart(ax)
        elif option1 == 'Line':
           ax = px.line(p1, x= p1.index, y = ['L1','L2'])
           st.plotly_chart(ax)
        elif option1 == 'Scatter':
           ax = px.scatter(p1, x= p1.index, y = ['L1','L2'])
           st.plotly_chart(ax)
           
        #Team Leaders vs Avg AHT:
        p2= pd.pivot_table(df,values= 'AHT', index = 'Team Leader')
        option1 = st.radio(
             "Type Of Chart",
             ('Box', 'Line', 'Treemap'))

        if option1 == 'Box':
            ax = px.box(p2, x= p2.index, y = 'AHT')
            st.plotly_chart(ax)
        elif option1 == 'Line':
            ax = px.line(p2, x= p2.index, y = 'AHT')
            st.plotly_chart(ax)
        elif option1 == 'Treemap':
            ax = px.treemap(p2, path= [p2.index], values = 'AHT')
            st.plotly_chart(ax)   
        
        rate = st.slider('Please feel free to rate this app', 1, 5, 1)
        if st.button('Submit'):
            st.write('Feedback Recieved at 8667722919 & mukhthakannan@gmail.com.\n Thank you for the feedback.')

        image2 = Image.open('guru_image.jpg')
        st.image(image2, use_column_width=False)
	
if __name__ == '__main__':
	main()
