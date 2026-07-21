# Python Unit Converter

A modular Python application for converting Length and Temperature units using clean coding practices, input validation, logging, and exception handling.

---

## Project Overview

This project demonstrates software engineering best practices by implementing a console-based Unit Converter application with a modular architecture.

The application supports:

- Length Conversion
  - Meters → Feet
  - Feet → Meters

- Temperature Conversion
  - Celsius → Fahrenheit
  - Fahrenheit → Celsius

---

## Features

✔ Modular Design

✔ Exception Handling

✔ Logging

✔ Input Validation

✔ Clean Code Structure

✔ Easy to Extend

✔ Production Ready Folder Structure

✔ Python Best Practices

---

## Project Structure


UnitConverter/
│
├── main.py
├── length.py
├── temperature.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── tests/
│ ├── test_length.py
│ └── test_temperature.py
│
└── docs/
└── architecture.png


---

## Technologies Used

- Python 3.x
- Logging Module
- Exception Handling
- Modular Programming

---

## How to Run

Clone the repository

```bash
git clone https://github.com/<your-username>/UnitConverter.git
```

Navigate to the project

```bash
cd UnitConverter
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

## Sample Output

```
Enter conversion type (length / temperature / quit): length

Enter the value to convert:
10

Enter source unit:
meters

Enter target unit:
feet

Converted Value : 32.81 feet
```

---

## Error Handling

The application validates:

- Invalid conversion types
- Invalid numeric input
- Unsupported units
- Unexpected runtime exceptions

---

## Future Enhancements

- Weight Conversion
- Currency Conversion
- Volume Conversion
- GUI using Tkinter
- REST API using Flask/FastAPI
- Docker Support
- Unit Testing
- Configuration File Support

---

## Learning Outcomes

This project demonstrates:

- Modular Programming
- Function Design
- Logging
- Exception Handling
- Input Validation
- Python Best Practices
- Clean Architecture

---

## Author 

**Siddharth Navaneethan**

Data Engineer | Python | SQL | AWS | Snowflake | GCP
