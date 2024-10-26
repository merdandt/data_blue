import streamlit as st
import database_ddl as ddl
import prompt as pr
import sql_expert as se


st.set_page_config(page_title="SQL Expert Data Blue", page_icon="🐶")


# Initialize session state
if 'ddl' not in st.session_state:
    st.session_state['ddl'] = ''
if 'request' not in st.session_state:
    st.session_state['request'] = ''

# 1. Add image at the top
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("")

with col2:
    st.image("assets/blue.jpg", width=250)

with col3:
    st.write("")
    
st.header("Chat With Data Blue")

st.caption("Enter the DDL for the database in order for Data Blue to understand the content and the relationships between tables. \n Or choose from the datasets below.")

# Create columns for the buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("DPC University"):
        st.session_state.ddl = ddl.STUDENT

with col2:
    if st.button("DPC Antiques (employees)"):
        st.session_state.ddl = ddl.ANTIQUE

with col3:
    if st.button("Planet Dataset"):
        st.session_state.ddl = ddl.PLANET
    
# Clear DDL button
if st.button("Clear DDL",):
    st.session_state['ddl'] = ''

# Now render the text area after updating session state
ddl_input = st.text_area("Enter the DDL for the database", value=st.session_state['ddl'], height=200)
    
    
st.caption("Enter the DDL for the database so that Data Blue can understand the content and the relationships between tables. Or choose from the datasets below.")

request = st.text_input("Enter your request", key="request")

st.markdown("**For example:**")
st.markdown("""
- Show me all students from California.
- How do I get all students majoring in MIS and living in any state except New York?
- Using a GROUP BY clause, write an SQL statement that shows the top 3 hometowns of employees based on total salaries being paid. Use the TOP and ORDER BY clauses to solve.
""")

submit = st.button("Generate SQL Query")

if submit:
    if not ddl_input.strip():
        st.error("Please enter the DDL for the database before generating a SQL query.")
    else:
        with st.spinner("Generating SQL..."):
            try:
                sql = se.get_sql_from_text([ddl_input, pr.PROMPT_1], request)
                # Clean the SQL code
                sql = se.clean_sql_code(sql)
                # Use lowercase 'sql' for language
                st.code(sql, language='sql')  
            except Exception as e:
                st.error(f"An error occurred: {e}")
       
        
        
