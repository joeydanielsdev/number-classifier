from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()
@app.get("/api/classify-number")
def classify_number(number: int):
    if not isinstance(number, int):
        raise HTTPException(status_code=400, detail="Invalid input. Please provide a valid integer.")
    
    is_prime = is_prime_number(number)
    is_perfect = is_perfect_number(number)
    is_armstrong = is_armstrong_number(number)
    properties = []
    
    if is_armstrong:
        properties.append("armstrong")
    properties.append("odd" if number % 2 else "even")
    
    digit_sum = sum(int(digit) for digit in str(number))
    fun_fact = get_fun_fact(number)
    
    return {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }
# Helper functions (Implement logic for prime, perfect, and armstrong number checks)
def is_prime_number(n):
    # Implementation for checking prime number
    pass
def is_perfect_number(n):
    # Implementation for checking perfect number
    pass
def is_armstrong_number(n):
    # Implementation for checking armstrong number
    pass
def get_fun_fact(n):
    response = requests.get(f"http://numbersapi.com/{n}/math")
    return response.text if response.status_code == 200 else "No fun fact available"
