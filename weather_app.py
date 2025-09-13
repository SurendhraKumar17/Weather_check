{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "435d0c20-0bfc-463c-bce3-e9c58d055241",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "API_KEY = \"your_openweathermap_api_key\"\n",
    "BASE_URL = \"http://api.openweathermap.org/data/2.5/weather?\"\n",
    "\n",
    "def get_weather(city):\n",
    "    url = BASE_URL + \"appid=\" + API_KEY + \"&q=\" + city\n",
    "    response = requests.get(url)\n",
    "    data = response.json()\n",
    "\n",
    "    if data[\"cod\"] != \"404\":\n",
    "        main = data[\"main\"]\n",
    "        temp = main[\"temp\"] - 273.15  # Convert from Kelvin to Celsius\n",
    "        weather = data[\"weather\"][0][\"description\"]\n",
    "        print(f\"Weather in {city}: {weather}, {temp:.2f}°C\")\n",
    "    else:\n",
    "        print(\"City Not Found!\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    city = input(\"Enter city: \")\n",
    "    get_weather(city)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47fa00ae-c14f-4198-9f65-ea62d08c6adf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
