import requests

def get_supported_currencies() -> dict | None:
    url = "https://api.frankfurter.dev/v1/currencies"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.ConnectionError:
        return None
    return data

def get_exchange_rate(from_currency: str, to_currency: str, supported_currencies: dict | None = None) -> float | None:
    url = "https://api.frankfurter.dev/v1/latest"
    if supported_currencies is None:
        supported_currencies = get_supported_currencies()
    if supported_currencies is not None:
        allowed = supported_currencies.keys()
        if from_currency in allowed and to_currency in allowed:
            try:
                response = requests.get(url, params={"base": from_currency, "symbols": to_currency})
                response.raise_for_status()
                data = response.json()
            except requests.exceptions.HTTPError:
                return None
            except requests.exceptions.ConnectionError:
                return None
            return data['rates'][to_currency]
    return None
