# Natural Language to SQL Converter

Convert user natural language queries into SQL statements based on provided DDL using **Gemeni** and **Streamlit**.

## Overview

This project allows users to input queries in natural language and converts them into SQL queries based on a given database schema (DDL). It leverages the power of **Gemeni** for natural language processing and **Streamlit** for creating an interactive web application.

## Features

- **Natural Language Processing**: Translates user-friendly queries into SQL.
- **Custom DDL Input**: Users can provide their own database schema for accurate SQL generation.
- **Interactive Interface**: Built with Streamlit for ease of use.
- **Real-Time Conversion**: Instantaneous SQL query generation upon input.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Steps

1. **Clone the Repository**

```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Gemeni API
- Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and generate new Key
- Create `.streamlit/secrets.toml` file in the root of your project
- Paste `GOOGLE_API_KEY = "your-api-key"`

## Usage

### Run the Streamlit Application

```bash 
streamlit run app.py
```
### Provide DDL Input
- Paste your database schema (DDL) into the provided text area or
- Chose from templates
Example:
```bash
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);
```

#### Enter Natural Language Query
- Type your query in the input box.
Example:
```bash
List all employees in the Sales department earning more than $50,000.
```
