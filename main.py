from flask import Flask, request, jsonify

app = Flask(__name__)

subscriptions_list = []
subscription_id = 1

@app.route("/subscriptions", methods=["GET", "POST"])
def subscriptions():
    global subscription_id
    
    if request.method == "GET":
        return jsonify(subscriptions_list), 200
        
    elif request.method == "POST":
        data = request.get_json()
        new_subscription = {
            "id": subscription_id,
            "email": data["email"],
            "name": data["name"],
            "plan": data["plan"]
        }
        subscription_id += 1
        subscriptions_list.append(new_subscription)
        return jsonify(new_subscription), 201

if __name__ == "__main__":
    app.run(debug=True)