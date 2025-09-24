from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def main():
    return "Main"

@app.route("/subscriptions/<subscription_id>")
def get_subscription(subscription_id):
    subscription_data = {
        "id": subscription_id,
        "email": "carmen.kilbourne@gmail.com",
        "name": "Carmen",
        "plan": "standard"
    }
    return jsonify(subscription_data), 200

if __name__ == "__main__":
    app.run(debug=True)