# Conversational Data Query Chatbot

This project is a **Conversational Chatbot** designed to interact with users in natural language to query and retrieve insights from two datasets (historical and forecasted). The chatbot processes user queries, analyzes the data, and responds with actual values derived from the datasets.

## Features
1. **Natural Language Query Understanding**:
   - Interprets user queries using the LLaMA language model.
2. **Data Retrieval and Processing**:
   - Performs data operations on historical and forecasted datasets.
3. **Human-Readable Responses**:
   - Returns results in natural language, making it easy to understand.
4. **Scalable and Extensible**:
   - Easily add new datasets or expand query capabilities.

---

## Datasets
The chatbot uses two datasets:

1. **Forecasted Dataset**:
   - Year: 2025
   - Columns: Year, Month, Base/Project, LOBGroup, CostCategory, Forecasted Plan Rate

2. **Historical Dataset**:
   - Years: 2021–2024
   - Columns: Year, Month, Base/Project, LOBGroup, CostCategory, Plan Rate

The datasets share common columns and can be used for comparative analysis, aggregation, and filtering.

---

## Prerequisites
- Python 3.8 or later
- **pip** for managing Python packages

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AnkitaKrishnan/Conversational-data-query-chatbot.git
   cd conversational-data-query-chatbot
   ```

2. **Set Up a Virtual Environment** (Optional but Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install Required Libraries**:
   Install all dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify PyTorch Installation**:
   For macOS (CPU-only):
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
   ```

5. **Download the Datasets**:
   Place the datasets (`forecasted_dataset.csv` and `historical_dataset.csv`) in the project directory.

---

## Running the Project

1. **Start the Flask Server**:
   Run the chatbot server:
   ```bash
   python chatbot.py
   ```

2. **Access the API**:
   The server will run on `http://127.0.0.1:5000`.

---

## How to Use the Chatbot

You can interact with the chatbot by sending POST requests to the `/chat` endpoint.

### Example 1: Using cURL
```bash
curl -X POST http://127.0.0.1:5000/chat \
-H "Content-Type: application/json" \
-d '{"query": "What is the total forecasted plan rate for Base in 2025?"}'
```

### Example 2: Using Python
```python
import requests

url = "http://127.0.0.1:5000/chat"
payload = {"query": "What is the average historical plan rate for LOB_Group_1?"}

response = requests.post(url, json=payload)
print(response.json())
```

### Example 3: Using Postman
1. Open Postman and create a new POST request.
2. Set the URL to `http://127.0.0.1:5000/chat`.
3. Add a JSON body:
   ```json
   {
       "query": "Compare the forecasted and historical average plan rates for LOB_Group_3."
   }
   ```
4. Send the request to receive a response.

---

## Example Queries
1. **"What is the total forecasted plan rate for Base in 2025?"**
   - Response: `"The total forecasted plan rate for Base in 2025 is $5,000,000."`

2. **"What is the average historical plan rate for LOB_Group_1?"**
   - Response: `"The average historical plan rate for LOB_Group_1 (2021-2024) is $12,300."`

3. **"Compare the forecasted and historical average plan rates for LOB_Group_3."**
   - Response: `"Historical average for LOB_Group_3: $15,000, Forecasted average: $18,500."`

---

## Project Structure
```
├── chatbot.py              # Main Python script to run the chatbot server
├── forecasted_dataset.csv  # Forecasted dataset
├── historical_dataset.csv  # Historical dataset
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

---

## Customization
1. **Add New Datasets**:
   - Include new datasets in the `chatbot.py` file and update the logic in `execute_data_query()`.

2. **Extend Query Handling**:
   - Add new query patterns in `execute_data_query()` to support more use cases.

3. **Fine-Tune the LLaMA Model**:
   - Use custom training data to improve the chatbot’s query interpretation.

---

## Troubleshooting

1. **PyTorch Installation Issues**:
   - Ensure you’re using the correct version for macOS (CPU-only):
     ```bash
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
     ```

2. **Server Not Running**:
   - Verify that Flask is installed:
     ```bash
     pip install flask
     ```
   - Ensure no other process is using port `5000`.

3. **Dataset Not Found**:
   - Ensure the `forecasted_dataset.csv` and `historical_dataset.csv` files are in the project directory.

---

## Contributing
If you’d like to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with detailed changes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---
