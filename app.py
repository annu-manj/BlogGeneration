import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import ctransformers


#Function to get response from LLAma 2 model
def getLLamaresponse(input_text,no_words,blog_style):

    # llm model
    llm = ctransformers.CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config = {'max_new_tokens':256,
                                  'temperature':0.01})
    

    # Prompts template
    template = """Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words."""
    
    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_words"], template = template)

    ## Genrate the response form the LLama 2 model
    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))

    print(response)
    return response

st.set_page_config(page_title="Generate Blogs")

st.header("Generate Blog")

input_text = st.text_input("Enter the blog topic")

## creating columns
col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of words")
with col2:
    blog_style = st.selectbox("Writing the blog for ", ('Researches', 'data scientist','common people'))

submit = st.button("generate")

if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))