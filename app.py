import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from PIL import Image
import plotly.express as px

#@st.cache
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
        
        
        df = pd.read_csv('E:/Sitel/sitel_csv.csv')
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
            
        df1 = px.data.tips()
        fig = px.box(df1, x="day", y="total_bill", color="smoker",title = "guru's boxplot",height= 600,width=900)
        fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default
        st.plotly_chart(fig) 
        
        rate = st.slider('Please feel free to rate this app', 1, 5, 1)
        if st.button('Submit'):
            st.write('Feedback Recieved at 8667722919 & mukhthakannan@gmail.com.\n Thank you for the feedback.')

        #image2 = Image.open('guru_image.jpg')
        #st.image(image2, use_column_width=False)
        
        df2 = pd.DataFrame({'col1': [1,2,3]})
        st.dataframe(df2)  
        st.table(df2)
        #st.dataframe(df.style.highlight_max(axis=0))
        st.text('This is some text.')
        st.markdown('Streamlit is **_really_ cool**.')
        st.write('Hello, *World!* :sunglasses:')
        st.title('This is a title')
        st.header('This is a header')
        st.subheader('This is a subheader')
        code = '''def hello():
        print("Hello, Streamlit!")'''
        st.code(code, language='python')
        
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
        st.line_chart(chart_data)
        st.area_chart(chart_data)
        st.bar_chart(chart_data)
        
        df = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
        st.map(df)
        
        from PIL import Image
        image = Image.open('guru_image.jpg')
        st.image(image, caption='Image',use_column_width=False)
        
        agree = st.checkbox('I agree')
        if agree:
            st.write('Great!')
            
        genre = st.radio(
        "What's your favorite movie genre",
        ('Comedy', 'Drama', 'Documentary'))
   
        if genre == 'Comedy':
            st.write('You selected comedy.')
        else:
            st.write("You didn't select comedy.")
            
        option = st.selectbox(
            'How would you like to be contacted?',
            ('Email', 'Home phone', 'Mobile phone'))
       
        st.write('You selected:', option)
        options = st.multiselect(
            'What are your favorite colors',
            ['Green', 'Yellow', 'Red', 'Blue'],
            ['Yellow', 'Red'])
       
        age = st.slider('How old are you?', 0, 130, 25)
        st.write("I'm ", age, 'years old')

        values = st.slider(
            'Select a range of values',
            0.0, 100.0, (25.0, 75.0))
        st.write('Values:', values)
        
        title = st.text_input('Movie title', 'Life of Brian')
        st.write('The current movie title is', title)
        
        number = st.number_input('Insert a number')
        st.write('The current number is ', number)
        
        txt = st.text_area('Text to analyze', '''
        It was the best of times, it was the worst of times, it was
        the age of wisdom, it was the age of foolishness, it was
        the epoch of belief, it was the epoch of incredulity, it
        was the season of Light, it was the season of Darkness, it
        was the spring of hope, it was the winter of despair, (   )
        ''')
        #st.write('Sentiment:', run_sentiment_analysis(txt))
        
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            st.write(data)
            
        #color = st.beta_color_picker('Pick A Color', '#00f900')
        #st.write('The current color is', color)
        
        add_selectbox = st.sidebar.selectbox(
            "How would you like to be contacted??",
            ("Email", "Home phone", "Mobile phone")
        )
        with st.echo():
            st.write('This code will be printed')
        
        
        st.write('Progress bar')
        import time
        my_bar = st.progress(0)
        for percent_complete in range(3):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)

        st.write('Spinner')
        with st.spinner('Wait for it'):
            time.sleep(1)
        st.success('Done!')
        
        st.balloons()
        st.error('This is an error')
        st.warning('This is a warning')
        st.info('This is a purely informational message')
        st.success('This is a success message!')
        e = RuntimeError('This is an exception of type RuntimeError')
        st.exception(e)
        
        st.help(pd.DataFrame)
        
        st.write('Append Option')
        df1 = pd.DataFrame(
        np.random.randn(5, 5),
        columns=('col %d' % i for i in range(5)))
        my_table = st.table(df1)
        df2 = pd.DataFrame(
        np.random.randn(5, 5),
        columns=('col %d' % i for i in range(5)))
        my_table.add_rows(df2)
       
        my_chart = st.line_chart(df1)
        my_chart.add_rows(df2)
        
        
        
	
if __name__ == '__main__':
	main()
