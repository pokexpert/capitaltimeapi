from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)


AUTHORIZED_TOKENS = {"secrettoken123", "anothertoken456"}


capital_timezones = {
    "Seoul": "Asia/Seoul",
    "Washington": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Paris": "Europe/Paris",
    "Canberra": "Australia/Sydney",
    "Ottawa": "America/Toronto",
}

@app.route("/time", methods=["GET"])
def get_time():
    token = request.headers.get("Authorization")
    if token not in AUTHORIZED_TOKENS:
        return jsonify({"error": "Unauthorized: Invalid token."}), 401

    capital = request.args.get("capital")
    if not capital:
        return jsonify({"error": "Missing 'capital' query parameter."}), 400

    tz_name = capital_timezones.get(capital)
    if not tz_name:
        return jsonify({"error": f"City '{capital}' not in database."}), 404

    tz = pytz.timezone(tz_name)
    now = datetime.now(tz)
    utc_offset = now.strftime('%z')
    utc_offset_formatted = f"{utc_offset[:3]}:{utc_offset[3:]}"  # "+0900" → "+09:00"

    return jsonify({
        "capital": capital,
        "timezone": tz_name,
        "local_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "utc_offset": utc_offset_formatted
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)