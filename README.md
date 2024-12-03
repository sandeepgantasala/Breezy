
# **Breezy**  
A simple and user-friendly web application to get real-time weather updates and a 5-day forecast for any city.

## **Features**
- **Current Weather**: Displays the current temperature, weather conditions, and descriptions.
- **5-Day Forecast**: Provides a detailed 5-day weather forecast with temperatures, conditions, and icons.
- **Temperature Units**: Toggle between **Celsius (°C)** and **Fahrenheit (°F)** for both current weather and forecast.
- **City Search**: Enter any city to get weather updates instantly.
- **Dynamic Icons**: Displays weather condition icons fetched from the OpenWeatherMap API.
- **Clean UI**: Minimalist design with a responsive layout for seamless usage.

---

## **Technologies Used**
- **Backend**: Django Framework
- **Frontend**: HTML, CSS (with Django Templates)
- **Weather API**: OpenWeatherMap API

---

## **Installation**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/sandeepgantasala/Breezy.git
cd breezy
```

### **Step 2: Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

### **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 4: Configure the API Key**
1. Copy the `.env.example` file to a new `.env` file:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and replace `your_openweathermap_api_key_here` with your actual OpenWeatherMap API key:
   ```plaintext
   OPENWEATHER_API_KEY=your_actual_api_key
   ```

3. Ensure your `views.py` file reads the API key from the environment variable using the `python-decouple` package:
   ```python
   from decouple import config

   api_key = config('OPENWEATHER_API_KEY')
   ```

### **Step 5: Run the Application**
```bash
python manage.py runserver
```

### **Step 6: Access the Application**
Open your browser and go to:
```
http://127.0.0.1:8000/
```

---

## **Usage**
1. Enter a city name in the search bar.
2. Toggle between Celsius and Fahrenheit using the dropdown menu.
3. View real-time weather updates or switch to the 5-day forecast tab.

---

## **Project Structure**
```
Breezy/
│
├── BreezyBackend/             # Project settings
├── breezyapp/                 # Main app
│   ├── templates/             # HTML templates
│   ├── migrations/            # Database migrations
│   ├── views.py               # Backend logic
│   ├── urls.py                # URL routing
│   └── models.py              # Data models (if any)
│
├── .env.example               # Example environment configuration
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django project management
├── requirements.txt           # Python dependencies
└── README.md                  # Documentation (this file)
```

---

## **Screenshots**
### **Home Page**
<img width="1470" alt="Screenshot 2024-12-03 at 1 40 03 PM" src="https://github.com/user-attachments/assets/5c0a99c1-c8ec-4dc0-86fb-b3cb45709c0d">


### **5-Day Forecast**
<img width="1470" alt="Screenshot 2024-12-03 at 1 39 43 PM" src="https://github.com/user-attachments/assets/ed933dd9-b163-49c9-843f-993edd1a9b88">

---

## **Contributors**
- [Kore Shiva Nagendra Babu](https://github.com/shivanagendrak)
