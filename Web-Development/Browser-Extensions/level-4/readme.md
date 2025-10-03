# Level 4: API Integration

Build professional-grade extensions that integrate external APIs and services. These projects involve asynchronous operations, authentication, background processing, and real-time data handling.

## Project Options

### Option 1: GitHub Stats Viewer
Display GitHub statistics and repository information from the toolbar.

**Features:**
- User profile statistics
- Repository stars/forks overview
- Contribution graph
- Recent activity feed
- OAuth authentication
- Real-time data updates

**Technical Requirements:**
- GitHub REST API integration
- OAuth 2.0 authentication flow
- Background service worker for API calls
- Data caching strategy
- Rate limiting handling
- Chart/graph visualization

**API Endpoint:** `https://api.github.com/users/{username}`

### Option 2: Weather Dashboard
Real-time weather information with location detection.

**Features:**
- Current weather conditions
- 5-day forecast
- Multiple location support
- Automatic location detection
- Weather alerts
- Temperature unit conversion

**Technical Requirements:**
- OpenWeatherMap or WeatherAPI integration
- Geolocation API
- Background updates
- Error handling for API failures
- Data refresh intervals
- Icon/image handling

**API Endpoint:** `https://api.openweathermap.org/data/2.5/weather`

### Option 3: Currency Converter
Real-time currency conversion with multiple currencies.

**Features:**
- Live exchange rates
- Multiple currency support
- Historical rate charts
- Favorite currencies
- Offline mode with cached rates
- Auto-update rates

**Technical Requirements:**
- Exchange rate API integration
- Background periodic updates
- Offline data handling
- Chart library integration
- Number formatting
- API key management

**API Endpoint:** `https://api.exchangerate-api.com/v4/latest/USD`

## Submission Requirements

Create a folder `ProjectName_YourGitHubUsername` containing:

1. **manifest.json** with host permissions
2. **background.js** - API calls and data processing
3. **popup.html/js** - User interface
4. **api.js** - API wrapper functions
5. **config.js** - Configuration (API keys template)
6. **.env.example** - Environment variables template
7. **styles.css** - Professional styling
8. **README.md** - Setup guide with API key instructions

## API Integration Example
```
// background.js
async function fetchData(url) {
try {
const response = await fetch(url, {
headers: {
'Authorization': Bearer ${API_KEY}
}
});
if (!response.ok) throw new Error('API request failed');
return await response.json();
} catch (error) {
console.error('Error fetching data:', error);
return null;
}
}

// Message passing
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
if (request.action === 'fetchData') {
fetchData(request.url).then(sendResponse);
return true; // Async response
}
});
```


## Security Considerations

- Never commit API keys to repository
- Use environment variables or config files
- Include `.env.example` with placeholder keys
- Document API key setup in README
- Implement rate limiting
- Handle authentication securely

## Learning Resources

- [Fetch API Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [Chrome Extension Host Permissions](https://developer.chrome.com/docs/extensions/mv3/declare_permissions/)
- [Background Service Workers](https://developer.chrome.com/docs/extensions/mv3/service_workers/)
- [OAuth 2.0 Flow](https://developer.chrome.com/docs/extensions/mv3/tut_oauth/)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [OpenWeatherMap API](https://openweathermap.org/api)

## Evaluation Criteria

- API integration quality
- Error handling robustness
- Authentication implementation
- Data caching strategy
- User experience
- Code organization
- Security practices
- Documentation completeness

