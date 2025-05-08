# GPT+ Quant MVP

This is a lightweight MVP (Minimum Viable Product) system that combines GPT-based analysis with real-time market data to support early-morning trading decisions for individual traders.


## Features

- Analyze the market direction within the first 5 minutes after the U.S. stock market opens.
- Combine structured technical data (open, high, low, close, volume) with simulated news sentiment.
- Output directional judgment, entry recommendation, and entry price range using GPT analysis.
- Data source: [Polygon.io](https://polygon.io) free API.


## How to Use

1. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Create a file named `apikey.txt` in the project root with the following format:

    ```bash
    OPENAI_API_KEY=your_openai_key
    POLYGON_API_KEY=your_polygon_key
    ```

3. Run the main script:

    ```bash
    python main.py
    ```

4. Follow the prompts to enter:
    - Target stock symbol (e.g., `QQQ`)
    - Analysis date (e.g., `2024-05-01`)
    The program will return GPT-generated insight based on technical and news context.


## Project Structure

  ```text
  gpt_quant_mvp/
  ├── main.py                 # Entry point for running the program
  ├── check_models.py         # Script to list accessible GPT models
  ├── gpt_analyzer.py         # GPT prompt generation and OpenAI API access
  ├── prompt_templates.py     # Prompt formatting templates
  ├── data_fetcher.py         # Unified interface to choose data source
  ├── data_fetcher_polygon.py # Polygon.io data fetcher
  ├── output.py               # Formats and prints analysis results
  ├── apikey.txt              # Stores API keys (ignored by Git)
  ├── .gitignore              # Excludes secrets and cache from Git
  └── README.md               # Project overview and usage instructions
  ```

## Security Note

- Do not commit your `apikey.txt` to version control. It must be listed in `.gitignore`.
- This project is an experimental prototype. It is not production-grade and should not be used for live trading decisions.


## Roadmap

- Add real-time data support (Webull, Alpaca, or other providers)
- Auto-select best available data source
- Add chart and UI-based output
- Add multi-strategy GPT comparison and scoring


## License

MIT License. Free to use for educational and personal experimental purposes.
