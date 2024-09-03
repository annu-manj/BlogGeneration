# BlogGeneration

Streamlit web application designed for generating blog posts with the assistance of the LLama 2 language model. Users input the topic, desired word count, and select a style or category for the post. The application defines a function, getLLamaresponse, which orchestrates the interaction with the LLama 2 model, creating a prompt based on user inputs and retrieving a response.

## Streamlit:  
  
A Python library used for creating web applications. It provides an interactive interface where users can input parameters and see results in real-time.
In this project, Streamlit handles the user interface, including text inputs, drop-down menus, and buttons.  

## LangChain:  
  
A framework designed for working with large language models (LLMs). In this project, it's used to manage prompts and communicate with the LLaMA 2 model.
LLaMA 2 Model via ctransformers:

The core LLM used to generate the blog content. Specifically, the project uses a LLaMA 2 model, which is a highly capable transformer-based language model.  
The ctransformers library is used to load and interact with the model. It enables efficient handling of model inference, supporting quantized versions to optimize memory usage.


## To Run
streamlit run app.py
