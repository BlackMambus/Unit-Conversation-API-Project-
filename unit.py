from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(title="Unit Conversion API")

# Conversion factors
conversion_factors = {
    "length": {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    },
    "weight": {
        "kilogram": 1.0,
        "gram": 0.001,
        "milligram": 0.000001,
        "pound": 0.453592,
        "ounce": 0.0283495
    }
}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Unit Conversion API!"}

@app.get("/convert")
def convert(
    category: str,
    from_unit: str,
    to_unit: str,
    value: float
):
    category = category.lower()
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if category not in conversion_factors:
        raise HTTPException(status_code=400, detail="Invalid category")

    units = conversion_factors[category]
    if from_unit not in units or to_unit not in units:
        raise HTTPException(status_code=400, detail="Invalid units for the given category")

    # Convert to base unit, then to target unit
    base_value = value * units[from_unit]
    converted_value = base_value / units[to_unit]

    return {
        "category": category,
        "from": from_unit,
        "to": to_unit,
        "original_value": value,
        "converted_value": converted_value
    }
