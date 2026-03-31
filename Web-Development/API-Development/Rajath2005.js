// Weather Info Fetcher using Open-Meteo API (no API key required)
// Contributed by Rajath Kiran | github.com/Rajath2005

async function getWeather(latitude, longitude) {
  const url = `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`;

  try {
    const response = await fetch(url);
    const data = await response.json();
    const weather = data.current_weather;

    console.log(`Temperature : ${weather.temperature}°C`);
    console.log(`Wind Speed  : ${weather.windspeed} km/h`);
    console.log(`Weather Code: ${weather.weathercode}`);
  } catch (error) {
    console.error("Failed to fetch weather:", error.message);
  }
}

// Example: Bangalore coordinates
getWeather(12.9716, 77.5946);