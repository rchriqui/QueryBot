from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert at converting english questuib to sql query
    the name of the database is best_countries_2024 the columns
    are population_2024, population_growthRate, land_area, 
    country, region, unMember, population_density, population_densityMi, share_borders, Hdi2020, WorldHappiness2022, Hdi2021.
    
    Noting thatHdi2021 is The Human Development Index, or HDI, is a metric compiled by the United Nations Development Programme and used to quantify a country's "average achievement in three basic dimensions of human development: a long and healthy life, knowledge, and a decent standard of living.
    share_borders: Share Borders With other Country
    population_densityMi:Population Density per Mile
    population_density: Population Density Per KM.
    
    Example1: How many entries of records are present? The SQL command will be something SELECT COUNT(*) FROM best_countries_2024 
    
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]


## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"best_countries_2024.db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)

