
from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class QuoteRequest(BaseModel):
    full_name: str
    address: str
    last4_ssn: str
    loan_type: str

class QuoteResponse(BaseModel):
    current_balance: float
    current_rate: float
    new_rate: float
    current_payment: float
    new_payment: float
    monthly_savings: float
    total_savings_estimate: float
    message: str

def calculate_monthly_payment(principal, annual_rate, term_months):
    r = (annual_rate / 100) / 12
    payment = principal * (r * (1 + r) ** term_months) / ((1 + r) ** term_months - 1)
    return round(payment, 2)

@app.post("/get-quote", response_model=QuoteResponse)
def get_quote(request: QuoteRequest):
    current_balance = random.randint(15000, 30000) if request.loan_type == "Auto" else random.randint(200000, 400000)
    current_rate = round(random.uniform(5.5, 7.5), 2)
    new_rate = 4.5

    if request.loan_type == "Auto":
        current_payment = calculate_monthly_payment(current_balance, current_rate, 60)
        new_payment = calculate_monthly_payment(current_balance, new_rate, 60)
    else:
        current_payment = calculate_monthly_payment(current_balance, current_rate, 360)
        new_payment = calculate_monthly_payment(current_balance, new_rate, 360)

    monthly_savings = round(current_payment - new_payment, 2)
    total_savings_estimate = round(monthly_savings * (60 if request.loan_type == "Auto" else 360), 2)

    return QuoteResponse(
        current_balance=current_balance,
        current_rate=current_rate,
        new_rate=new_rate,
        current_payment=current_payment,
        new_payment=new_payment,
        monthly_savings=monthly_savings,
        total_savings_estimate=total_savings_estimate,
        message=f"Congratulations {request.full_name}! You could save ${monthly_savings}/month by refinancing."
    )
