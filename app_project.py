#                                                                 RESUME APP
import streamlit as st
import pandas as pd

st.sidebar.title('Navigation')
section = st.sidebar.radio("Go to ",['About','Skills','Experience','Education','Contact'])

skills = {
    'Python':0.8,
    'Machine Learning':0.3,
    'Data Visualization':0.3,
    'DSA':0.3,
    'Codeforces':0.3,
    'Leetcode':0.3,
    "SQL":0.3
}
st.title('Quantum')
st.subheader('Data Scientist')


if section == 'About':
    st.markdown("""
    Experienced Data Scientist with strong skills in analytics,machine learning,and storytelling with data.
    Passionate about turning data into actionable insights.
    """)


elif section == 'Skills':
    st.header('Skills Overview ')
    for skill , level in skills.items():
        st.write(skill)
        st.progress(level)
    df_skills = pd.DataFrame({
        "Skills":list(skills.keys()),
        "Proficiency":list(skills.values())
    })    
    st.bar_chart(df_skills.set_index("Skills"))

elif section == 'Experience':
    st.header('Work Experience')

    with st.expander(f"Data Scientist | DSA  | DP | ML DL | Agentic Ai | CP"):
        st.write(f"""
        -100+ Questions on Codeforces

        -50+ Questions on DSA
         
        -32+ Lectures on ML

        -3+ Projects on ML

        -Built 5 streamlit app in production

        -Built 30+ Dashboards for risk and underwriting

        -Developed 20 DBT Models      
""")
        with st.expander(f"Materials Engineering | Quantum Mechanics"):
                st.write(f"""

                -60+ Lectures on Quantum Mechanics

                -Worked extensively on development of new materials
                
        """)


elif section == 'Education':
     st.header('Education')

     with st.expander(f" Primary Education "):
          st.write(f"""

            - DAV Public School Lakhisarai (X)

 """)
     with st.expander(f" Secondary Education "):
              st.write(f"""
    
                - Shri Sheshnag Uchh vidyalaya Lakhisarai (XII) 
    
     """)      
     with st.expander(f" Graduation "):
              st.write(f"""
                - B.Tech in Metallurgical and Materials Engineering 

                - National Institute of Technology Jamshedpur 
    
     """)


elif section == 'Contact':
      st.header('Get in touch')
      col1,col2 = st.columns(2)
      with col1:
            email = st.text_input("Email")
            phone = st.text_input("contact number")

      with col2:
            linkedin_id = st.text_input("Linkedin ID URL")
            Discord = st.text_input("Discord link")

      
      message = st.text_area("Message")
      if st.button("Send"):
            st.success('Thanks for reaching out , much obliged')



























