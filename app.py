import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from flask import Flask, request, jsonify

# Step 1: Load the Data
# Replace with your actual CSV file paths
forecasted_df = pd.read_csv("forecasted_data_2025.csv")
historical_df = pd.read_csv("HistoricalData.csv")

# Step 2: Load the LLaMA Model
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
nlp_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Metadata Context for Query Understanding
metadata_context = """
You are a chatbot designed to answer questions about two datasets:
1. Forecasted dataset for 2025 with columns: Year, Month, Base/Project, LOBGroup, CostCategory, and Forecasted Plan Rate.
2. Historical dataset from 2021 to 2024 with columns: Year, Month, Base/Project, LOBGroup, CostCategory, and Plan Rate.

Both datasets share the same categorical and temporal columns.
Always respond with actual numerical or textual results derived from the data.
"""

# Step 3: LLaMA Query Interpretation
def interpret_query(user_query):
    prompt = f"""
    {metadata_context}

    User Query: "{user_query}"
    Extract the intent and provide a structured response on how to handle the query programmatically.
    """
    response = nlp_pipeline(prompt, max_length=512, num_return_sequences=1)
    return response[0]["generated_text"]

# Step 4: Execute Data Query
def execute_data_query(interpreted_response, user_query):
    if "forecasted" in user_query.lower() and "total" in user_query.lower():
        if "Base" in user_query:
            result = forecasted_df[forecasted_df["Base/Project"] == "Base"]["Forecasted Plan Rate"].sum()
            return f"The total forecasted plan rate for Base in 2025 is {result}."
        elif "Project" in user_query:
            result = forecasted_df[forecasted_df["Base/Project"] == "Project"]["Forecasted Plan Rate"].sum()
            return f"The total forecasted plan rate for Project in 2025 is {result}."
    elif "historical" in user_query.lower() and "average" in user_query.lower():
        if "LOB_Group_1" in user_query:
            result = historical_df[historical_df["LOBGroup"] == "LOB_Group_1"]["Plan Rate"].mean()
            return f"The average historical plan rate for LOB_Group_1 (2021-2024) is {result}."
    elif "compare" in user_query.lower() and "forecasted" in user_query.lower():
        lob_group = user_query.split("LOB_Group_")[1][0]  # Extract the LOB group number
        historical_avg = historical_df[historical_df["LOBGroup"] == f"LOB_Group_{lob_group}"]["Plan Rate"].mean()
        forecast_avg = forecasted_df[forecasted_df["LOBGroup"] == f"LOB_Group_{lob_group}"]["Forecasted Plan Rate"].mean()
        return f"Historical average for LOB_Group_{lob_group}: {historical_avg}, Forecasted average: {forecast_avg}."
    else:
        return "I'm sorry, I couldn't process your query. Could you rephrase?"

# Step 5: Generate Chatbot Response
def chatbot_response(user_query):
    # Use LLaMA to interpret the query
    interpreted_response = interpret_query(user_query)
    print(f"Interpreted Response: {interpreted_response}")

    # Execute the query on the datasets
    response = execute_data_query(interpreted_response, user_query)
    return response

# Step 6: Flask API for Interaction
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get("query")
    response = chatbot_response(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
