import google.generativeai as genai
import streamlit as st


genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])


def get_sql_from_text(prompt_list, question):
    model = genai.GenerativeModel(model_name="gemini-pro")
    full_prompt = '\n'.join(prompt_list) + '\n' + question
    response = model.generate_content(full_prompt)
    return response.text


def clean_sql_code(sql):
    # Remove code block markers if present
    if sql.startswith("```"):
        sql = sql.strip('`')  # Remove leading and trailing backticks
        lines = sql.split('\n')
        # Remove language specifier if present
        if lines[0].lower() in ['sql', 'sql\n']:
            lines = lines[1:]
        sql = '\n'.join(lines)
    return sql