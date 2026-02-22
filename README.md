# Currency Converter CLI

A command-line currency converter that fetches live exchange rates 
using the Frankfurter API. Supports a wide range of world currencies.

## Requirements
- Python 3.10 or above
- requests (`pip install requests`)

## How to Run
```
git clone https://github.com/apathydevil/currency-converter-cli
cd currency-converter-cli
pip install -r requirements.txt
python main.py
```

## Features
- Live exchange rates fetched from the Frankfurter API
- Full list of supported currencies fetched directly from the API
- Optional currency listing before converting
- Input validation for currencies and amounts
- Clean error handling for network issues

## APIs Used
- [Frankfurter](https://frankfurter.dev/) — free, no API key required

## What I Learned
Reinforced API calls and error handling, learned to 
fetch dynamic data instead of hardcoding static lists, and practiced 
splitting code across multiple files with a clean separation between 
API logic and application logic.