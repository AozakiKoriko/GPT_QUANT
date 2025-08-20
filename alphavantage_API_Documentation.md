# Alpha Vantage API Documentation

> Free JSON APIs for realtime and historical stock market data & options data with over 50 technical indicators

## Table of Contents

- [Core Stock APIs](#core-stock-apis)
- [Options Data APIs](#options-data-apis)
- [Alpha Intelligence™](#alpha-intelligence)
- [Fundamental Data](#fundamental-data)
- [Forex (FX)](#forex-fx)
- [Cryptocurrencies](#cryptocurrencies)
- [Commodities](#commodities)
- [Economic Indicators](#economic-indicators)
- [Technical Indicators](#technical-indicators)

---

## Core Stock APIs

### Intraday <span class="popular-label">Trending</span>
Get intraday time series of the equity specified, covering extended trading hours where applicable.

**Endpoint:** `GET /query?function=TIME_SERIES_INTRADAY`

**Parameters:**
- `symbol` - The name of the equity of your choice
- `interval` - Time interval between two consecutive data points (1min, 5min, 15min, 30min, 60min)
- `apikey` - Your API key
- `outputsize` - compact (latest 100 data points) or full (full-length time series)
- `datatype` - json or csv

**Example Response:**
```json
{
    "Meta Data": {
        "1. Information": "Intraday (1min) open, high, low, close prices and volume",
        "2. Symbol": "IBM",
        "3. Last Refreshed": "2024-01-15 16:00:00",
        "4. Interval": "1min",
        "5. Output Size": "Compact",
        "6. Time Zone": "US/Eastern"
    },
    "Time Series (1min)": {
        "2024-01-15 16:00:00": {
            "1. open": "160.0000",
            "2. high": "160.0500",
            "3. low": "159.9500",
            "4. close": "160.0200",
            "5. volume": "1234"
        }
    }
}
```

### Daily
Get daily time series of the equity specified.

**Endpoint:** `GET /query?function=TIME_SERIES_DAILY`

**Parameters:**
- `symbol` - The name of the equity of your choice
- `apikey` - Your API key
- `outputsize` - compact (latest 100 data points) or full (full-length time series)
- `datatype` - json or csv

### Daily Adjusted <span class="popular-label">Trending</span>
Get daily time series (date, daily open, daily high, daily low, daily close, daily adjusted close, and daily volume) of the equity specified.

**Endpoint:** `GET /query?function=TIME_SERIES_DAILY_ADJUSTED`

### Weekly
Get weekly time series of the equity specified.

**Endpoint:** `GET /query?function=TIME_SERIES_WEEKLY`

### Weekly Adjusted
Get weekly adjusted time series of the equity specified.

**Endpoint:** `GET /query?function=TIME_SERIES_WEEKLY_ADJUSTED`

### Monthly
Get monthly time series of the equity specified.

**Endpoint:** `GET /query?function=TIME_SERIES_MONTHLY`

### Monthly Adjusted
Get monthly adjusted time series of the equity specified.

**Endpoint:** `GET /query?function=TIME_SERIES_MONTHLY_ADJUSTED`

### Quote Endpoint <span class="popular-label">Trending</span>
Get real-time quote data for a given stock symbol.

**Endpoint:** `GET /query?function=GLOBAL_QUOTE`

**Parameters:**
- `symbol` - The name of the equity of your choice
- `apikey` - Your API key

**Example Response:**
```json
{
    "Global Quote": {
        "01. symbol": "IBM",
        "02. open": "160.0000",
        "03. high": "161.5000",
        "04. low": "159.8000",
        "05. price": "160.5000",
        "06. volume": "1234567",
        "07. latest trading day": "2024-01-15",
        "08. previous close": "159.9000",
        "09. change": "0.6000",
        "10. change percent": "0.3752%"
    }
}
```

### Realtime Bulk Quotes <span class="premium-label">Premium</span>
Get real-time quote data for multiple stock symbols in a single API call.

**Endpoint:** `GET /query?function=GLOBAL_QUOTE_BULK`

### Ticker Search <span class="utility-label">🔧 Utility</span>
Search for best-matching symbols based on keywords.

**Endpoint:** `GET /query?function=SYMBOL_SEARCH`

**Parameters:**
- `keywords` - A text string of your choice
- `apikey` - Your API key

### Global Market Status <span class="utility-label">🔧 Utility</span>
Get the current market status (open/closed) of major exchanges.

**Endpoint:** `GET /query?function=MARKET_STATUS`

---

## Options Data APIs

### Realtime Options <span class="premium-label">Premium</span>
Get real-time options data for a given stock symbol.

**Endpoint:** `GET /query?function=OPTIONS_REALTIME`

### Historical Options <span class="popular-label">Trending</span>
Get historical options data for a given stock symbol.

**Endpoint:** `GET /query?function=OPTIONS_HISTORICAL`

---

## Alpha Intelligence™

### News & Sentiments <span class="popular-label">Trending</span>
Get latest news and sentiment analysis.

**Endpoint:** `GET /query?function=NEWS_SENTIMENT`

**Parameters:**
- `tickers` - Comma-separated list of tickers
- `topics` - Comma-separated list of topics
- `time_from` - Start time (YYYYMMDDTHHMMSS)
- `time_to` - End time (YYYYMMDDTHHMMSS)
- `sort` - Sort order (LATEST, EARLIEST, RELEVANCE)
- `limit` - Number of articles to return (max 200)
- `apikey` - Your API key

### Earnings Call Transcript
Get earnings call transcript for a given company.

**Endpoint:** `GET /query?function=EARNINGS_CALL_TRANSCRIPT`

### Top Gainers & Losers
Get top gainers and losers for a given market.

**Endpoint:** `GET /query?function=TOP_GAINERS_LOSERS`

### Insider Transactions <span class="popular-label">Trending</span>
Get insider transactions for a given company.

**Endpoint:** `GET /query?function=INSIDER_TRANSACTIONS`

### Analytics (Fixed Window)
Get analytics data with fixed time window.

**Endpoint:** `GET /query?function=ANALYTICS_FIXED_WINDOW`

### Analytics (Sliding Window)
Get analytics data with sliding time window.

**Endpoint:** `GET /query?function=ANALYTICS_SLIDING_WINDOW`

---

## Fundamental Data

### Company Overview <span class="popular-label">Trending</span>
Get company information, financial ratios, and other key metrics.

**Endpoint:** `GET /query?function=OVERVIEW`

**Parameters:**
- `symbol` - The name of the equity of your choice
- `apikey` - Your API key

**Example Response:**
```json
{
    "Symbol": "IBM",
    "Asset Type": "Common Stock",
    "Name": "International Business Machines Corp",
    "Description": "International Business Machines Corp...",
    "CIK": "51143",
    "Exchange": "NYSE",
    "Currency": "USD",
    "Country": "USA",
    "Sector": "Technology",
    "Industry": "Information Technology Services",
    "Address": "1 New Orchard Road, Armonk, NY, United States",
    "Fiscal Year End": "December",
    "Latest Quarter": "2023-09-30",
    "Market Capitalization": "1234567890",
    "EBITDA": "123456789",
    "PERatio": "15.67",
    "PEGRatio": "1.23",
    "BookValue": "25.67",
    "DividendPerShare": "6.64",
    "DividendYield": "4.15",
    "EPS": "10.23",
    "RevenuePerShareTTM": "67.89",
    "ProfitMargin": "12.34",
    "OperatingMarginTTM": "15.67",
    "ReturnOnAssetsTTM": "8.90",
    "ReturnOnEquityTTM": "45.67",
    "RevenueTTM": "67890123456",
    "GrossProfitTTM": "34567890123",
    "DilutedEPSTTM": "10.23",
    "QuarterlyEarningsGrowthYOY": "12.34",
    "QuarterlyRevenueGrowthYOY": "8.90",
    "AnalystTargetPrice": "175.00",
    "TrailingPE": "15.67",
    "ForwardPE": "14.56",
    "PriceToBookRatio": "6.25",
    "PriceToSalesRatioTTM": "1.82",
    "EVToRevenue": "2.34",
    "EVToEBITDA": "12.34",
    "Beta": "1.23",
    "52WeekHigh": "185.00",
    "52WeekLow": "120.00",
    "50DayMovingAverage": "165.00",
    "200DayMovingAverage": "155.00",
    "SharesOutstanding": "987654321",
    "SharesFloat": "876543210",
    "SharesShort": "12345678",
    "SharesShortPriorMonth": "11111111",
    "ShortRatio": "1.23",
    "ShortPercentOutstanding": "1.25",
    "ShortPercentFloat": "1.41",
    "PercentInsiders": "0.12",
    "PercentInstitutions": "65.43",
    "ForwardAnnualDividendRate": "6.64",
    "ForwardAnnualDividendYield": "4.15",
    "PayoutRatio": "64.91",
    "DividendDate": "2023-12-09",
    "ExDividendDate": "2023-11-08",
    "LastSplitFactor": "2:1",
    "LastSplitDate": "1999-05-27"
}
```

### ETF Profile & Holdings
Get ETF profile and holdings information.

**Endpoint:** `GET /query?function=ETF_PROFILE`

### Corporate Action - Dividends
Get dividend information for a given company.

**Endpoint:** `GET /query?function=DIVIDENDS`

### Corporate Action - Splits
Get stock split information for a given company.

**Endpoint:** `GET /query?function=SPLITS`

### Income Statement
Get annual and quarterly income statements.

**Endpoint:** `GET /query?function=INCOME_STATEMENT`

### Balance Sheet
Get annual and quarterly balance sheets.

**Endpoint:** `GET /query?function=BALANCE_SHEET`

### Cash Flow
Get annual and quarterly cash flow statements.

**Endpoint:** `GET /query?function=CASH_FLOW`

### Earnings History
Get earnings history for a given company.

**Endpoint:** `GET /query?function=EARNINGS`

### Earnings Estimates <span class="popular-label">Trending</span>
Get earnings estimates for a given company.

**Endpoint:** `GET /query?function=EARNINGS_ESTIMATES`

### Listing & Delisting Status
Get listing and delisting status for securities.

**Endpoint:** `GET /query?function=LISTING_STATUS`

### Earnings Calendar
Get earnings calendar for upcoming earnings releases.

**Endpoint:** `GET /query?function=EARNINGS_CALENDAR`

### IPO Calendar
Get IPO calendar for upcoming initial public offerings.

**Endpoint:** `GET /query?function=IPO_CALENDAR`

---

## Forex (FX)

### Exchange Rates <span class="popular-label">Trending</span>
Get real-time exchange rates for currency pairs.

**Endpoint:** `GET /query?function=CURRENCY_EXCHANGE_RATE`

**Parameters:**
- `from_currency` - The currency you would like to convert from
- `to_currency` - The currency you would like to convert to
- `apikey` - Your API key

**Example Response:**
```json
{
    "Realtime Currency Exchange Rate": {
        "1. From_Currency Code": "USD",
        "2. From_Currency Name": "United States Dollar",
        "3. To_Currency Code": "EUR",
        "4. To_Currency Name": "Euro",
        "5. Exchange Rate": "0.8500",
        "6. Last Refreshed": "2024-01-15 16:00:00",
        "7. Time Zone": "UTC",
        "8. Bid Price": "0.8498",
        "9. Ask Price": "0.8502"
    }
}
```

### Intraday <span class="premium-label">Premium</span>
Get intraday time series for foreign exchange.

**Endpoint:** `GET /query?function=FX_INTRADAY`

### Daily
Get daily time series for foreign exchange.

**Endpoint:** `GET /query?function=FX_DAILY`

### Weekly
Get weekly time series for foreign exchange.

**Endpoint:** `GET /query?function=FX_WEEKLY`

### Monthly
Get monthly time series for foreign exchange.

**Endpoint:** `GET /query?function=FX_MONTHLY`

---

## Cryptocurrencies

### Exchange Rates <span class="popular-label">Trending</span>
Get real-time exchange rates for cryptocurrencies.

**Endpoint:** `GET /query?function=CURRENCY_EXCHANGE_RATE`

### Intraday <span class="premium-label">Premium</span>
Get intraday time series for cryptocurrencies.

**Endpoint:** `GET /query?function=DIGITAL_CURRENCY_INTRADAY`

### Daily
Get daily time series for cryptocurrencies.

**Endpoint:** `GET /query?function=DIGITAL_CURRENCY_DAILY`

### Weekly
Get weekly time series for cryptocurrencies.

**Endpoint:** `GET /query?function=DIGITAL_CURRENCY_WEEKLY`

### Monthly
Get monthly time series for cryptocurrencies.

**Endpoint:** `GET /query?function=DIGITAL_CURRENCY_MONTHLY`

---

## Commodities

### Crude Oil (WTI) <span class="popular-label">Trending</span>
Get real-time and historical data for WTI crude oil.

**Endpoint:** `GET /query?function=WTI`

### Crude Oil (Brent) <span class="popular-label">Trending</span>
Get real-time and historical data for Brent crude oil.

**Endpoint:** `GET /query?function=BRENT`

### Natural Gas
Get real-time and historical data for natural gas.

**Endpoint:** `GET /query?function=NATURAL_GAS`

### Copper <span class="popular-label">Trending</span>
Get real-time and historical data for copper.

**Endpoint:** `GET /query?function=COPPER`

### Aluminum
Get real-time and historical data for aluminum.

**Endpoint:** `GET /query?function=ALUMINUM`

### Wheat
Get real-time and historical data for wheat.

**Endpoint:** `GET /query?function=WHEAT`

### Corn
Get real-time and historical data for corn.

**Endpoint:** `GET /query?function=CORN`

### Cotton
Get real-time and historical data for cotton.

**Endpoint:** `GET /query?function=COTTON`

### Sugar
Get real-time and historical data for sugar.

**Endpoint:** `GET /query?function=SUGAR`

### Coffee
Get real-time and historical data for coffee.

**Endpoint:** `GET /query?function=COFFEE`

### Global Commodities Index
Get global commodities index data.

**Endpoint:** `GET /query?function=ALL_COMMODITIES`

---

## Economic Indicators

### Real GDP <span class="popular-label">Trending</span>
Get real GDP data.

**Endpoint:** `GET /query?function=REAL_GDP`

### Real GDP per Capita
Get real GDP per capita data.

**Endpoint:** `GET /query?function=REAL_GDP_PER_CAPITA`

### Treasury Yield <span class="popular-label">Trending</span>
Get treasury yield data.

**Endpoint:** `GET /query?function=TREASURY_YIELD`

### Federal Funds (Interest) Rate
Get federal funds rate data.

**Endpoint:** `GET /query?function=FEDERAL_FUNDS_RATE`

### CPI
Get Consumer Price Index data.

**Endpoint:** `GET /query?function=CPI`

### Inflation
Get inflation data.

**Endpoint:** `GET /query?function=INFLATION`

### Retail Sales
Get retail sales data.

**Endpoint:** `GET /query?function=RETAIL_SALES`

### Durable Goods Orders
Get durable goods orders data.

**Endpoint:** `GET /query?function=DURABLE_GOODS`

### Unemployment Rate
Get unemployment rate data.

**Endpoint:** `GET /query?function=UNEMPLOYMENT`

### Nonfarm Payroll
Get nonfarm payroll data.

**Endpoint:** `GET /query?function=NONFARM_PAYROLL`

---

## Technical Indicators

### SMA <span class="popular-label">Trending</span>
Simple Moving Average

**Endpoint:** `GET /query?function=SMA`

**Parameters:**
- `symbol` - The name of the equity of your choice
- `interval` - Time interval between two consecutive data points
- `time_period` - Number of data points used to calculate each moving average value
- `series_type` - The desired price type (close, open, high, low)
- `apikey` - Your API key

### EMA <span class="popular-label">Trending</span>
Exponential Moving Average

**Endpoint:** `GET /query?function=EMA`

### WMA
Weighted Moving Average

**Endpoint:** `GET /query?function=WMA`

### DEMA
Double Exponential Moving Average

**Endpoint:** `GET /query?function=DEMA`

### TEMA
Triple Exponential Moving Average

**Endpoint:** `GET /query?function=TEMA`

### TRIMA
Triangular Moving Average

**Endpoint:** `GET /query?function=TRIMA`

### KAMA
Kaufman Adaptive Moving Average

**Endpoint:** `GET /query?function=KAMA`

### MAMA
MESA Adaptive Moving Average

**Endpoint:** `GET /query?function=MAMA`

### VWAP <span class="premium-label">Premium</span>
Volume Weighted Average Price

**Endpoint:** `GET /query?function=VWAP`

### T3
Triple Exponential Moving Average (T3)

**Endpoint:** `GET /query?function=T3`

### MACD <span class="premium-label">Premium</span>
Moving Average Convergence/Divergence

**Endpoint:** `GET /query?function=MACD`

**Parameters:**
- `symbol` - The name of the equity of your choice
- `interval` - Time interval between two consecutive data points
- `series_type` - The desired price type (close, open, high, low)
- `fastlimit` - Fast EMA period (default: 0.02)
- `slowlimit` - Slow EMA period (default: 0.02)
- `apikey` - Your API key

**Example Response:**
```json
{
    "Meta Data": {
        "1: Symbol": "IBM",
        "2: Indicator": "Moving Average Convergence/Divergence (MACD)",
        "3: Last Refreshed": "2024-01-15",
        "4: Interval": "daily",
        "5: Series Type": "close",
        "6: Time Zone": "US/Eastern"
    },
    "Technical Analysis: MACD": {
        "2024-01-15": {
            "MACD": "1.2345",
            "MACD_Signal": "0.9876",
            "MACD_Hist": "0.2469"
        }
    }
}
```

### MACDEXT
MACD with controllable MA type

**Endpoint:** `GET /query?function=MACDEXT`

### STOCH <span class="popular-label">Trending</span>
Stochastic Oscillator

**Endpoint:** `GET /query?function=STOCH`

### STOCHF
Stochastic Fast

**Endpoint:** `GET /query?function=STOCHF`

### RSI <span class="popular-label">Trending</span>
Relative Strength Index

**Endpoint:** `GET /query?function=RSI`

### STOCHRSI
Stochastic Relative Strength Index

**Endpoint:** `GET /query?function=STOCHRSI`

### WILLR
Williams' %R

**Endpoint:** `GET /query?function=WILLR`

### ADX <span class="popular-label">Trending</span>
Average Directional Index

**Endpoint:** `GET /query?function=ADX`

### ADXR
Average Directional Index Rating

**Endpoint:** `GET /query?function=ADXR`

### APO
Absolute Price Oscillator

**Endpoint:** `GET /query?function=APO`

### PPO
Percentage Price Oscillator

**Endpoint:** `GET /query?function=PPO`

### MOM
Momentum

**Endpoint:** `GET /query?function=MOM`

### BOP
Balance of Power

**Endpoint:** `GET /query?function=BOP`

### CCI <span class="popular-label">Trending</span>
Commodity Channel Index

**Endpoint:** `GET /query?function=CCI`

### CMO
Chande Momentum Oscillator

**Endpoint:** `GET /query?function=CMO`

### ROC
Rate of Change

**Endpoint:** `GET /query?function=ROC`

### ROCR
Rate of Change Ratio

**Endpoint:** `GET /query?function=ROCR`

### AROON <span class="popular-label">Trending</span>
Aroon

**Endpoint:** `GET /query?function=AROON`

### AROONOSC
Aroon Oscillator

**Endpoint:** `GET /query?function=AROONOSC`

### MFI
Money Flow Index

**Endpoint:** `GET /query?function=MFI`

### TRIX
1-day Rate-Of-Change of a Triple Smooth EMA

**Endpoint:** `GET /query?function=TRIX`

### ULTOSC
Ultimate Oscillator

**Endpoint:** `GET /query?function=ULTOSC`

### DX
Directional Movement Index

**Endpoint:** `GET /query?function=DX`

### MINUS_DI
Minus Directional Indicator

**Endpoint:** `GET /query?function=MINUS_DI`

### PLUS_DI
Plus Directional Indicator

**Endpoint:** `GET /query?function=PLUS_DI`

### MINUS_DM
Minus Directional Movement

**Endpoint:** `GET /query?function=MINUS_DM`

### PLUS_DM
Plus Directional Movement

**Endpoint:** `GET /query?function=PLUS_DM`

### BBANDS <span class="popular-label">Trending</span>
Bollinger Bands

**Endpoint:** `GET /query?function=BBANDS`

**Parameters:**
- `symbol` - The name of the equity of your choice
- `interval` - Time interval between two consecutive data points
- `time_period` - Number of data points used to calculate each moving average value
- `series_type` - The desired price type (close, open, high, low)
- `nbdevup` - The standard deviation multiplier of the upper band (default: 2)
- `nbdevdn` - The standard deviation multiplier of the lower band (default: 2)
- `matype` - Moving average type (default: 0)
- `apikey` - Your API key

**Example Response:**
```json
{
    "Meta Data": {
        "1: Symbol": "IBM",
        "2: Indicator": "Bollinger Bands (BBANDS)",
        "3: Last Refreshed": "2024-01-15",
        "4: Interval": "daily",
        "5: Time Period": "20",
        "6: Series Type": "close",
        "7: Time Zone": "US/Eastern"
    },
    "Technical Analysis: BBANDS": {
        "2024-01-15": {
            "Real Upper Band": "165.0000",
            "Real Middle Band": "160.0000",
            "Real Lower Band": "155.0000"
        }
    }
}
```

### MIDPOINT
MidPoint over period

**Endpoint:** `GET /query?function=MIDPOINT`

### MIDPRICE
Midpoint Price over period

**Endpoint:** `GET /query?function=MIDPRICE`

### SAR
Parabolic SAR

**Endpoint:** `GET /query?function=SAR`

### TRANGE
True Range

**Endpoint:** `GET /query?function=TRANGE`

### ATR
Average True Range

**Endpoint:** `GET /query?function=ATR`

### NATR
Normalized Average True Range

**Endpoint:** `GET /query?function=NATR`

### AD <span class="popular-label">Trending</span>
Chaikin A/D Line

**Endpoint:** `GET /query?function=AD`

### ADOSC
Chaikin A/D Oscillator

**Endpoint:** `GET /query?function=ADOSC`

### OBV <span class="popular-label">Trending</span>
On Balance Volume

**Endpoint:** `GET /query?function=OBV`

### HT_TRENDLINE
Hilbert Transform - Instantaneous Trendline

**Endpoint:** `GET /query?function=HT_TRENDLINE`

### HT_SINE
Hilbert Transform - SineWave

**Endpoint:** `GET /query?function=HT_SINE`

### HT_TRENDMODE
Hilbert Transform - Trend vs Cycle Mode

**Endpoint:** `GET /query?function=HT_TRENDMODE`

### HT_DCPERIOD
Hilbert Transform - Dominant Cycle Period

**Endpoint:** `GET /query?function=HT_DCPERIOD`

### HT_DCPHASE
Hilbert Transform - Dominant Cycle Phase

**Endpoint:** `GET /query?function=HT_DCPHASE`

### HT_PHASOR
Hilbert Transform - Phasor Components

**Endpoint:** `GET /query?function=HT_PHASOR`

---

## API Usage Guidelines

### Rate Limits
- **Free API Key**: 5 API calls per minute and 500 API calls per day
- **Premium API Key**: 1200 API calls per minute and 575,000 API calls per day

### Base URL
```
https://www.alphavantage.co/query
```

### Authentication
All API calls require an `apikey` parameter. You can get a free API key by signing up at [Alpha Vantage](https://www.alphavantage.co/support/#api-key).

### Response Formats
- **JSON**: Default format, add `&datatype=json` (optional)
- **CSV**: Add `&datatype=csv` to get CSV format

### Error Handling
The API returns error messages in the following format:
```json
{
    "Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_INTRADAY."
}
```

### Best Practices
1. **Store API responses**: Cache data to avoid hitting rate limits
2. **Use appropriate intervals**: Choose time intervals based on your analysis needs
3. **Handle errors gracefully**: Implement proper error handling for failed requests
4. **Monitor usage**: Keep track of your API call count to stay within limits

---

## Code Examples

### Python
```python
import requests
import json

def get_stock_data(symbol, function, apikey):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": apikey
    }
    
    response = requests.get(url, params=params)
    return response.json()

# Example usage
apikey = "YOUR_API_KEY"
data = get_stock_data("IBM", "TIME_SERIES_DAILY", apikey)
print(json.dumps(data, indent=2))
```

### Node.js
```javascript
const axios = require('axios');

async function getStockData(symbol, function, apikey) {
    try {
        const response = await axios.get('https://www.alphavantage.co/query', {
            params: {
                function: function,
                symbol: symbol,
                apikey: apikey
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}

// Example usage
const apikey = 'YOUR_API_KEY';
getStockData('IBM', 'TIME_SERIES_DAILY', apikey)
    .then(data => console.log(JSON.stringify(data, null, 2)));
```

### PHP
```php
<?php
function getStockData($symbol, $function, $apikey) {
    $url = "https://www.alphavantage.co/query";
    $params = http_build_query([
        "function" => $function,
        "symbol" => $symbol,
        "apikey" => $apikey
    ]);
    
    $response = file_get_contents($url . "?" . $params);
    return json_decode($response, true);
}

// Example usage
$apikey = "YOUR_API_KEY";
$data = getStockData("IBM", "TIME_SERIES_DAILY", $apikey);
echo json_encode($data, JSON_PRETTY_PRINT);
?>
```

### C#
```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;

public class AlphaVantage
{
    private readonly HttpClient _client;
    private readonly string _baseUrl = "https://www.alphavantage.co/query";
    
    public AlphaVantage()
    {
        _client = new HttpClient();
    }
    
    public async Task<dynamic> GetStockDataAsync(string symbol, string function, string apikey)
    {
        var url = $"{_baseUrl}?function={function}&symbol={symbol}&apikey={apikey}";
        var response = await _client.GetStringAsync(url);
        return JsonConvert.DeserializeObject(response);
    }
}

// Example usage
var alphaVantage = new AlphaVantage();
var data = await alphaVantage.GetStockDataAsync("IBM", "TIME_SERIES_DAILY", "YOUR_API_KEY");
Console.WriteLine(JsonConvert.SerializeObject(data, Formatting.Indented));
```

---

## Support & Resources

- **Documentation**: [https://www.alphavantage.co/documentation/](https://www.alphavantage.co/documentation/)
- **API Key Signup**: [https://www.alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key)
- **Terms of Service**: [https://www.alphavantage.co/terms_of_service/](https://www.alphavantage.co/terms_of_service/)
- **Privacy Policy**: [https://www.alphavantage.co/privacy/](https://www.alphavantage.co/privacy/)
- **Contact**: [https://www.alphavantage.co/support/](https://www.alphavantage.co/support/)

---

*Copyright © Alpha Vantage Inc. 2017-2025*
