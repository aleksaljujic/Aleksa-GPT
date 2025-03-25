import streamlit as st
from datetime import datetime
import os
import openai
from PIL import Image
from dotenv import load_dotenv, dotenv_values

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key
about_file = "About.txt"

logo = Image.open("C:\\Users\\aleks\\AleksaGPT\\AlexaGPT\\aleksa_logo.png")

content = '''
According to text that is provided below this sentence answer questions about Aleksa.

My CV:

name: Aleksa

role: student

[NAME]  
Aleksa Ljujić  

[CONTACT]  
+381 60333 4933  
aleksa.jlujic2@gmail.com  
https://www.linkedin.com/in/aleksaljujic  
https://github.com/aleksaljujic  

[EDUCATION]  
Faculty of Organizational Sciences (2021 – Present)  
- Information Systems and Technologies  
- Relevant Coursework: Artificial Intelligence, Machine Learning  

Technical School, Čačak (2017 – 2021)  
- Information Systems and Technologies  

[EXPERIENCE]  
Integration Architect Intern – STADA GIS Serbia (february 2024 – april 2024)  
- SAP: Gained foundational ERP knowledge and SAP environment navigation  
- LeanIX: Maintained interface data accuracy and quality  
- Power BI: Created data visualizations and dashboards  
- Enterprise Architecture: Collaborated with architects on solution design  
- Designed data flow diagrams for interfaces  
- Contributed to SAP Trading Partner Management and API Management projects  

[PROJECTS]  
Intelligent Weather Prediction Using Neural Networks  
- Technologies: PyTorch, Pandas, NumPy  
- Developed neural network model for temperature prediction using historical weather data  

Student Performance Predictor  
- Technologies: Scikit-learn, Pandas, Jupyter Notebook  
- Built ML model to forecast exam outcomes with 85% accuracy  

Pharmacy Billing System (Server/Client Application)  
- Technologies: .NET, SQL Server  
- Created local network application for streamlined pharmacy transactions  

Multiplayer Air Hockey Game  
- Technologies: Unity, C#, Photon  
- Implemented real-time networking with Photon for synchronized gameplay  

[SKILLS]  
Programming: Java, C#, Python, SQL, C, HTML/CSS, JavaScript  
AI/ML: PyTorch, Scikit-learn, Pandas, NumPy, Data Analysis  
Tools: SAP, LeanIX, Power BI, Adobe Photoshop/Illustrator  
Architecture: Enterprise Architecture, Data Flow Design, API Management  
Soft Skills: Critical Thinking, Problem-Solving, Time Management  

[STUDENT ORGANIZATIONS]
1) Student Organization FONIS (2022 – Present)
Project Companies to Students (C2S) (2022 – 2023) Human Resources team member
What I did:
- Organization and management of selection processes for project delegates
- Conducting internal trainings and workshops for organization members
- Monitoring member development and satisfaction through feedback sessions
- Organizing team events and team-building activities
--------------------------------   
Project Students to Students (S2S) (2022 – 2023) Design team member
What I did:
- Creation of visual identity for events and projects
- Design of promotional materials (posters, brochures, social media content)
- Work with tools like Adobe Photoshop, Illustrator and Figma
- Collaboration with PR team on visual content
--------------------------------
Hackathon for High School Students (HZS) (2022 – 2023) Logistics team member
What I did:
- Event organization (venue, technical equipment, logistical support)
- Coordination with partners and sponsors regarding event needs
- Budget management and material procurement for projects
- Solving unexpected problems during events
--------------------------------
Project Students to Students (S2S) (2022 – 2023) Corporate Relations team member
What I did:
- Communication with companies and potential sponsors
- Writing and sending partnership and sponsorship proposals
- Organization of guest lectures and workshops with companies
- Design (S2S)
- Logistics (HZS)
- Corporate relations (S2S)

2) Student organization Student Union – Faculty of Organizational Sciences (2023 – 2024)  
IT & Design Team member for Projects like Practice Day, GreenWay, Sport Bizz, KSON
What I did:
- Creation of visual identity for events and projects
- Design of promotional materials (posters, brochures, social media content)
- Work with tools like Adobe Photoshop, Illustrator and Figma
- Collaboration with PR team on visual content

[LANGUAGES]  
English (Fluent)  
Serbian (Native)  '''

# Custom CSS for chat bubbles
st.markdown("""
<style>
    .user-message {
        padding: 10px;
        border-radius: 15px;
        margin: 5px;
        background-color: #e6f3ff;
        max-width: 70%;
        float: right;
        clear: both;
        color: black;
    }
    .bot-message {
        padding: 10px;
        border-radius: 15px;
        margin: 5px;
        background-color: #f0f0f0;
        max-width: 70%;
        float: left;
        clear: both;
        color: black;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def display_chat():
    """Display chat messages with appropriate styling"""
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', 
                        unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message">{message["content"]}</div>', 
                        unsafe_allow_html=True)

def simple_bot_response(user_input):
    """Basic response logic (replace with your actual bot logic)"""
    responses = {
        "hello": "Hello! How can I help you today?",
        "help": "I'm here to assist you. What do you need help with?",
        "bye": "Goodbye! Have a great day!"
    }
    
    user_input = user_input.lower()
    return responses.get(user_input, 
        "I'm still learning! Could you rephrase that?")

def chatbot(content, user_input):
    user_input = user_input.lower()     
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content":  "You are a helpful assistant."},
            {"role": "user", "content": f"Here is some context: {content}"},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content


# App layout

header = st.container()  # Creates a dedicated space for header

with header:
    # Create two columns (1: logo, 4: title - adjust ratio as needed)
    logo_col, title_col = st.columns([1, 4])
    
    with logo_col:
        if logo:  # Only show if logo was loaded
            st.image(logo, width=100)  # Adjust width as needed
    
    with title_col:
        st.title(" Aleksa GPT")

st.write("Welcome to Aleksa GPT")
st.write("Ask everything you want to know about Alexa")

# Display chat history
display_chat()

# User input at bottom
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to history
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input,
        "timestamp": datetime.now().isoformat()
    })
    
    # Get bot response
    bot_response = chatbot(content, user_input)
    
    # Add bot response to history
    st.session_state.chat_history.append({
        "role": "bot",
        "content": bot_response,
        "timestamp": datetime.now().isoformat()
    })
    
    # Rerun to update display
    st.rerun()