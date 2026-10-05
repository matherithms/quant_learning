def momentum(prices, window=20):
    """Calculate momentum returns."""
    return prices / prices.shift(window) - 1