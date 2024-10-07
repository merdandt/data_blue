from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai
import database_ddl as ddl
import prompt as pr

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_sql_from_text(prompt_list, question):
    model = genai.GenerativeModel(model_name="gemini-pro")
    full_prompt = '\n'.join(prompt_list) + '\n' + question
    response = model.generate_content(full_prompt)
    return response.text

st.set_page_config(page_title="SQL Expert Data Blue", page_icon="🇹🇲")

# 1. Add image at the top
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("")

with col2:
    st.image("assets/tako.png", width=150)

with col3:
    st.write("")
st.header("Chat With Data Blue")

st.caption("Enter the DDL for the database in order for Data Blue to understand the content and the relationships between tables. \n Or choose from the datasets below.")

# 2. Modify buttons to autofill DDL
if st.button("DPC University"):
    st.session_state.ddl = ddl.STUDENT
if st.button("DPC Antiques (employees)"):
    st.session_state.ddl = ddl.ANTIQUE
if st.button("Planet Dataset"):
    st.session_state.ddl = ddl.PLANET

# 3. Make ddl_input clearable
ddl_input = st.text_area("Enter the DDL for the database", key="ddl", height=200)

st.caption("Enter the natural language request and Data Blue will convert it to an SQL query.")

request = st.text_input("Enter your request", key="request")

st.caption("For example: \n Show me all students from California. \n How to get all students majoring in MIS and living in any state except New York \n Using a GROUP BY Clause, write an SQL statement that shows the TOP 3 hometowns of Employees based on total salaries being paid. Use the TOP and ORDER BY Clause to solve.")

submit = st.button("Generate SQL Query")

if submit:
    sql = get_sql_from_text([ddl_input, pr.PROMPT_1], request)
    print(sql)
    st.write(sql)