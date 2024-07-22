#cosoft Task 1 := chatbot
# AI Internship
import streamlit as st

st.set_page_config(page_title="AI Chatbot",page_icon="")
st.title(":violet[AI Chat Fusion ]")
GROQ_API_KEY="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"

st.sidebar.title(":violet[Navigation]")

page = st.sidebar.selectbox(":blue[Choose a page]", ["ChatBoat"])

if page == "ChatBoat":
    
    #for the Api 
    from groq import Groq

    # It offers a pre-built approach to manage the back-and-forth 
    # exchange between the user and the LLM model.
    from langchain.chains import conversation
    from langchain_groq import ChatGroq
    from langchain.chains.conversation.memory import ConversationBufferMemory
    from langchain.chains import ConversationChain
    from langchain.prompts import PromptTemplate
    from dotenv import load_dotenv
    from groq import Groq
    import  os

    load_dotenv()
    GROQ_API_KEY="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"
    groq_api_key = GROQ_API_KEY
    
    def main():
                     
            st.subheader(":blue[ChatBoat App]")
            st.write("----")
          
            conversation_memory_length = st.sidebar.slider(':blue[Conversational Meomory Length:]',1,10,value=5)
            
            memory = ConversationBufferMemory(k=conversation_memory_length)
            
            user_question  = st.text_area(":black[Ask A Question...]")
             
            if 'chat_history' not in st.session_state:
                st.session_state.chat_history=[]
                #1
                st.session_state.selected_question = None
            else:
                for message in st.session_state.chat_history:
                    memory.save_context({'input':message['human']},{'output':message['AI']})
                    
            groq_chat = ChatGroq(        
            groq_api_key  = groq_api_key,
            model_name = "mixtral-8x7b-32768")
            
            conversation = ConversationChain(
                llm = groq_chat,
                memory = memory
                
            )
            if user_question:
                if st.session_state.selected_question is None:

                    response = conversation(user_question)
                    message = {'human':user_question,'AI':response['response']}

                    st.session_state.chat_history.append(message)

                    st.write("Chatbot : ",response['response'])
            
                else:
                    st.write(":green[select from chat history]")
            selected_question_index = st.selectbox('Select Question from History',[message['human'] for message in st.session_state.chat_history],index=None if st.session_state.selected_question is None else [message['human'] for message in st.session_state.chat_history].index(st.session_state.selected_question))


            if selected_question_index is not None :
                    st.session_state.selected_question = selected_question_index
                    selected_response = [message['AI'] for message in st.session_state.chat_history if message['human'] == selected_question_index][0]
                    st.write("Chatbot : ",selected_response)
        
            
            
    if __name__  == '__main__':
        main()

