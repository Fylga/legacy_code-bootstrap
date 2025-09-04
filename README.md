# Legacy Code - Bootstrap: Cobol X Copilot Project

This repository contains a simple COBOL application that simulates a basic accounting system. The application allows users to view their balance, credit their account, debit their account, and exit the program. The goal of this project is to demonstrate how to work with legacy COBOL code and gradually refactor it into a modern Python application using test-driven development (TDD) principles.

## Features

- View Current Balance
- Credit Account
- Debit Account
- Persistent Storage of Balance
- Input Validation and Error Handling

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)
- venv (for creating virtual environments)

### Installation

```bash
cd python-accounting-app
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -e .
pip install -r requirements.txt
```

### Running the Application

```bash
python src/main.py
```
### Running Tests

```bash
pytest --cov=src --cov-report=term-missing tests
```
