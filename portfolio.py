# Install Streamlit before running
# pip install streamlit

import streamlit as st
import base64
import nbformat
from nbconvert import HTMLExporter

# Create columns for the image and the title/subtitle
col1, col2 = st.columns([1, 3])

# Column for image
with col1:
    st.image("My-Profile-Picture.jpg", width=170)  # Adjust the width as needed

# Column for title and subtitle
with col2:
    st.title("Ali Basit - AI Engineer Portfolio")
    st.subheader("Artificial Intelligence Engineer | Data Scientist | Automation Specialist")

# # Creating two columns for the image and contact information
# col1, col2 = st.columns([1, 2])

# # Left column for the image
# with col1:
#     st.image("My-Profile-Picture.jpg", caption="Ali Basit")

# Contact Information with Links
st.header("Contact Information")
st.markdown("""
- [GitHub](https://github.com/MuziSan07)
- [LinkedIn](https://www.linkedin.com/in/alibasit02/)
- [Gmail](mailto:shumailhaider678@gmail.com)
- [WhatsApp](https://wa.me/923554458467)
""")

# About Me Section
st.header("About Me")
st.write("""
    Innovative AI Engineer with expertise in automating customer-facing processes and building predictive models that drive business insights. 
    Skilled in developing AI-driven solutions, including NLP-based voice and text support systems, customer support automation, and risk analysis models. 
    Strong analytical mindset with a passion for leveraging AI to optimize business processes and improve customer satisfaction. 
    Dedicated to delivering scalable, efficient AI and data solutions that align with organizational goals.
""")

# Skills Section
st.header("Skills")
st.write("""
- **AI & Machine Learning**: Dialogflow, IBM Watson, Microsoft Bot Framework, Twilio, NLP, predictive modeling, scoring models
- **Programming**: Python, SQL, R
- **Data Analysis**: Statistical analysis, data mining, data cleaning, trend analysis, pattern recognition
- **Automation Tools**: Zapier, Integromat, API integration
- **Data Visualization**: Tableau, Power BI
- **Industry Knowledge**: CRM, risk assessment, credit scoring, automotive industry experience
- **Soft Skills**: Collaboration, communication, cross-functional teamwork
""")

# Technical Experience Section
st.header("Experience")

# AI Automation Specialist Experience
st.subheader("AI Automation Specialist for Sales and Customer Support")
st.write("""
- **Automated Sales Processes**: Designed AI-driven workflows to guide users through the buying process, from inquiries to final sale, enhancing customer experience.
- **Payment Collection System**: Built a secure, user-friendly system to automate payment reminders and answer related queries, improving efficiency.
- **Customer Support Automation**: Developed NLP models for 24/7 customer support, handling inquiries about insurance, warranty, and service appointments.
- **Omnichannel Communication**: Created seamless communication workflows across email, text, and voice platforms, ensuring customers received prompt and personalized responses.
- **Workflow Optimization**: Monitored and refined AI-driven processes to meet customer satisfaction benchmarks.
""")

# Data Scientist Experience
st.subheader("Data Scientist – Risk Analysis and Customer Scoring Models")
st.write("""
- **Data Extraction and Preparation**: Extracted and cleaned data from multiple sources for accurate risk analysis, categorizing data to identify customer behavior patterns.
- **Risk Factor Identification**: Applied statistical and data mining techniques to identify key indicators related to customer charge-offs and payment patterns.
- **Scoring Model Development**: Built and refined predictive scoring models for customer risk assessment, implementing machine learning algorithms to enhance underwriting decisions.
- **Cross-Functional Collaboration**: Worked with underwriting, finance, and customer support teams to align risk models with business needs.
""")

# Certifications Section
st.header("Certifications")
st.write("""
- **Google Career Certificate in IT Automation** – Focus on Python Automation, creating efficient scripts for business process automation.
- **Artificial Intelligence and Data Science Diploma** – NUST, SEECS: Covered machine learning, data analysis, and AI-driven solutions.
- **Google Career Certificate in Cyber Security** – Understanding of data security, essential for AI applications in customer data handling and compliance.
""")

# Education Section
st.header("Education")
st.write("""
- **Bachelor of Science in Artificial Intelligence** *(in progress)*  
  Virtual University, Pakistan  
  *(Expected Graduation: 2027)*
  
- **Intermediate**  
  Public School and College, Pakistan  
  *(2021 - 2023)*
  
- **Matriculation**  
  Army Public School and College, Pakistan  
  *(2018 - 2020)*
""")

# Projects Section
st.header("Projects")
st.write("""
- **AI Customer Support Bot**: Developed a conversational AI bot for FAQs and booking services using Dialogflow and Twilio.
- **Credit Scoring Model for Risk Analysis**: Built a predictive model identifying high-risk customers by analyzing past payment behaviors, reducing potential charge-offs by 20%.
- **Omnichannel AI Communication System**: Designed an integrated system across email, text, and voice channels using IBM Watson for NLP, increasing customer engagement by 30%.
""")

# Additional Skills Section
st.header("Additional Skills")
st.write("""
- **Interpersonal**: Strong communication and teamwork skills to collaborate effectively with stakeholders.
- **Analytical Mindset**: Ability to interpret and adjust AI models based on data-driven insights.
- **Industry Tools**: Familiarity with CRM platforms and automotive software, enabling seamless integration with sales and customer support solutions.
""")

st.write("Thank you for visiting my portfolio! For any inquiries or collaborations, feel free to reach out.")

# Adding images at the end of the portfolio side by side
col1, col2 = st.columns(2)
with col1:
    st.image("My_dev_2.jfif", caption="Development Snapshot 1")
with col2:
    st.image("My_dev.jfif", caption="Development Snapshot 2" , width= 680)

# Display a button that shows the PDF embedded in the page
st.header("Working Experience at Geo Labs")
if st.button('View Working Experience Certificate'):
    with open("./Working Experience.pdf", "rb") as file:
        base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)
if st.button('View Working Certificate'):
    with open("./My Certificate.pdf", "rb") as file:
        base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

st.header("Projects")

notebooks = {
    "Credit Scoring Model": "b_Code_CreditScoring.ipynb",
    "EDA on Sales Data": "EDA_sales_data.ipynb",
    "New Applications Credit Score Predictions": "f3_NewApplications_CreditScore_Predictions.ipynb",
    "Prediction Model": "Prediction_Model.ipynb",
    "Segmentation Model": "segmentation_Model.ipynb",
    "Anomaly Detection": "Anamoly Detection.ipynb"
}

for title, file_path in notebooks.items():
    if st.button(f'View {title}'):
        # Read the notebook
        with open(file_path, "r", encoding="utf-8") as file:
            nb = nbformat.read(file, as_version=4)
        
        # Convert to HTML
        html_exporter = HTMLExporter()
        html_exporter.template_name = 'classic'
        body, _ = html_exporter.from_notebook_node(nb)
        
        # Encode HTML for embedding
        base64_html = base64.b64encode(body.encode('utf-8')).decode('utf-8')
        html_display = f'<iframe src="data:text/html;base64,{base64_html}" width="700" height="1000"></iframe>'
        st.markdown(html_display, unsafe_allow_html=True)
        #https://github.com/MuziSan07/portfolio-streamlit..git