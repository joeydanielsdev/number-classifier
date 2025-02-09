📊 Number Facts API
An API that takes a number as input and returns interesting mathematical properties, such as prime status, factors, and more—along with a fun fact!

🚀 Features
Check if a number is prime, even, or odd
Get the factorial, Fibonacci sequence, and other properties
Receive a fun fact about the number
Supports JSON responses
📦 Installation
Clone the repository
bash
Copy
Edit
git clone https://github.com/yourusername/number-facts-api.git
cd number-facts-api
Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
▶️ Usage
Run the API
bash
Copy
Edit
python app.py
Example Request
Send a GET request to:

bash
Copy
Edit
http://localhost:5000/number/42
Example Response
json
Copy
Edit
{
  "number": 42,
  "is_prime": false,
  "is_even": true,
  "factorial": "Too large to compute",
  "fibonacci": false,
  "fun_fact": "42 is the answer to life, the universe, and everything."
}
🔧 API Endpoints
Method	Endpoint	Description
GET	/number/{num}	Returns properties and facts of {num}
🛠 Technologies
Python (Flask/FastAPI)
Math & Number Theory
Fun Fact Dataset
🤝 Contributing
Fork the repo and create a new branch:
bash
Copy
Edit
git checkout -b feature-branch
Make changes and commit:
bash
Copy
Edit
git commit -m "Added new feature"
Push and create a pull request.