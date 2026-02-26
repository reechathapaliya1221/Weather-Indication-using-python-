# Weather-Indication-using-python-
A desktop weather application that displays current weather data for Nepali districts using OpenWeatherMap API
# Weather App

This is a simple desktop weather application built with Python and Tkinter. It allows users to select a district in Nepal and get the current weather information using the OpenWeatherMap API.

## Features

- Select a district from a dropdown list.
- Displays current weather climate, description, temperature, pressure, and humidity.
- User-friendly graphical interface.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your API Key:**
    - Create a free account on [OpenWeatherMap](https://openweathermap.org/) to get an API key.
    - Create a file named `.env` in the project's root directory.
    - Add your API key to the `.env` file like this:
      ```
      API_KEY=your_actual_api_key_here
      ```

4.  **Run the application:**
    ```bash
    python <your-main-python-file-name>.py
    ```
