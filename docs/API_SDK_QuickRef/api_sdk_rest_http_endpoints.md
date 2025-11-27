
# 📘 Notes on SDK, API, REST API, HTTP Calls, and Endpoints

---

## 1. Environment Variables

- **Definition**: Key-value pairs stored in the OS (Operating System) environment.  
- **Purpose**: Programs and SDKs read them at runtime to decide behavior.  
- **Example**:  
  ```python
  os.environ['ANONYMIZED_TELEMETRY'] = 'False'
  ```
  - Tells IBM watsonx SDK whether telemetry data should be anonymized.  
- **General use cases**: API keys, config paths, tracking URIs, device settings.

ANOTHER EXAMPLE:

```python
import os

# Set environment variable
os.environ['DB_CONNECTION'] = 'postgresql://user:password@localhost:5432/mydatabase'

# Later in your code, retrieve it
db_url = os.environ['DB_CONNECTION']
print("Connecting to:", db_url)
```

- Key: DB_CONNECTION

- Value: the database connection string.

- Usage: Your script or SDK can read this variable to know how to connect to the database, without hard‑coding sensitive info in the code.

---

## 2. API (Application Programming Interface)
- **Definition**: A set of rules/contracts for communication between software components.  
- **Form**: Functions, methods, or endpoints.  
- **Example**: IBM Cloud API endpoint `POST /generate_text`.  
- **Key idea**: API = *the interface* (the “doorway” to a system).

---

## 3. SDK (Software Development Kit)
- **Definition**: A **toolbox/package** that wraps APIs and provides developer‑friendly tools.  
- **Contents**: Libraries, classes, utilities, documentation.  
- **Example**: IBM watsonx SDK (`ibm_watsonx_ai`) provides `ModelInference`.  
- **Role**: SDK uses APIs internally, but exposes clean Python methods.  
- **Analogy**: SDK = dashboard + controls to drive the API easily.

---

## 4. REST API
- **Definition**: A _design style for building APIs using HTTP_.  
- **Principles**:
  - Resources (users, orders, models) exposed via URLs.  
  - Standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`).  
  - Stateless (each request is independent, can not recall/remember earlier request).  
  - JSON/XML for resource representation.  
- **Example**:  
  - `GET /users/123` → fetch user info  
  - `POST /orders` → make/genrate order  

---

## 5. HTTP Call
- **Definition**: The raw request sent using the HTTP protocol.  
- **Components**: Method (GET/POST), URL, headers, body.  
- **Example** (Python `requests`):
  ```python
  response = requests.post("https://api.example.com/generate",
                           headers={"Authorization": "Bearer token"},
                           json={"input": "Hello"})
  ```
- **Key idea**: REST APIs are *built on top of* HTTP calls.

---

## 6. Endpoint
- **Definition**: A specific URL where an API action happens.  
- **Base URL vs Endpoint**:
  - Base: `https://api.example.com/`  
  - Endpoint: `https://api.example.com/users/123`  
- **Role**: Endpoint = the “address” of the resource/action.  
- **In SDKs**: You don’t see endpoints directly; the SDK calls them internally.

---

## 7. Putting It All Together (Flow)

```
Your Python Code
   |
   v
SDK (ibm_watsonx_ai)
   - Classes like ModelInference
   - Wraps API calls
   |
   v
REST API Endpoint (URL)
   - e.g. https://api.watsonx.ibm.com/v1/generate
   |
   v
HTTP Call
   - POST request with headers + JSON
   |
   v
IBM Cloud Service
   - Processes request, returns response
   |
   v
Your Python Code (receives result)
```

---

## 8. Side‑by‑Side Example

**Raw HTTP (manual):**
```python
import requests
url = "https://api.watsonx.ibm.com/v1/generate"
headers = {"Authorization": "Bearer <api_key>", "Content-Type": "application/json"}
payload = {"model_id": "some-model-id", "input": "Hello world"}
response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

**SDK (simplified):**
```python
from ibm_watsonx_ai.foundation_models import ModelInference
model = ModelInference(model_id="some-model-id")
result = model.generate_text(prompt="Hello world")
print(result)
```

---

## ✅ Key Takeaways
- **Environment variable** = global config knob.  
- **API** = communication rules/contracts.  
- **SDK** = toolbox wrapping APIs for easier use.  
- **REST API** = structured style of using HTTP for resources.  
- **HTTP call** = the raw request/response transport.  
- **Endpoint** = the specific URL where the API action happens.  
- **SDK vs API**: SDK simplifies API usage; API is the underlying contract.  
- **REST vs HTTP**: REST is a design style; HTTP is the protocol it uses.

---