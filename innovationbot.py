import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
from llama_index.evaluation import ResponseEvaluator
from pathlib import Path
from PIL import Image

openai.api_key = st.secrets.api_credentials.openai_key

image_path = Path('images/logo.png')
logo = Image.open(image_path)
st.set_page_config(
    page_title="Innovation Bot",
    page_icon=logo,
)
with st.sidebar:
    image_path = Path('images/logo1.png')
    logo = Image.open(image_path)
    st.image(logo)
    st.title("Welcome to Waterstons Innovation bot!")
    st.markdown("This chatbot will answer all of your questions about Innovation.")
    st.markdown("For more information about our team and what we get up to please check out our **substack:** https://waterstonsinnovation.substack.com/")

image_path = Path('images/robot_dog.png')
image1 = Image.open(image_path)
st.image(image1, use_column_width=True)
st.header("Welcome to the Waterstons Innovation Bot 💬 ")

if "messages" not in st.session_state.keys(): # Initialize the chat message history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about the Innovation Team's Substack articles!"}
    ]


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the Innovation Team's knowledge – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on the Waterstons Innovation team's blog posts and your job is to answer technical questions. Assume that all questions are related to the innovation team's blog posts, and only provide answers with information from these blogs. Keep your answers technical and based on facts – do not hallucinate blog posts. Include in your response a link to the relavant article."))
        evaluator = ResponseEvaluator(service_context=service_context)
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index, evaluator

index, evaluator = load_data()
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True, )

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

image_path = Path('images/assistant.png')
assistant_img = Image.open(image_path)
image_path = Path('images/user.png')
user_img = Image.open(image_path)
        # If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant", avatar=assistant_img):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            # print(response.source_nodes[0].metadata["file_name"])
            # print(response.source_nodes[0].score)
            # print(response.source_nodes[0])
            eval_result = evaluator.evaluate_response(prompt, response)
            print(str(eval_result.passing))
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
            