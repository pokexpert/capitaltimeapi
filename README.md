# Capital City Time API
This API returns the current local time and UTC offset for a given capital city and is secured with an 
authorization token.

GET http://34.48.171.198:8080/time?capital=CityName

**Authorization**
The authorization tokens are secrettoken123 or token123.

**Example**
curl -H "Authorization: secrettoken123" "http://34.48.171.198:8080/time?capital=Seoul"

**Supported Cities**
Seoul
Washington
London
Tokyo
Paris
Canberra
Ottawa
