from flask import Flask, request, jsonify
    
plan_types = ["standard", "deluxe"]  

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
        email = (data.get("email") or "").strip()
        name = (data.get("name") or "").strip()
        plan = (data.get("plan") or "").strip().lower()

        if "@" not in email:
            return jsonify({"error": "El email debe contener @"}), 400
        if not name:
            return jsonify({"error": "Name cannot be empty"}), 400
        if not plan:
            return jsonify({"error": "plan cannot be empty"}), 400
            
        if plan not in plan_types:
            return jsonify({
                "error": f"Only valid plans are: {plan_types}"
            }), 400

        new_subscription = {
            "id": subscription_id,
            "email": email,
            "name": name,
            "plan": plan
        }

        subscription_id += 1
        subscriptions_list.append(new_subscription)
        return jsonify(new_subscription), 201
    

@app.route("/subscriptions/<int:subscription_id>", methods=["GET"])
def get_subscription_with_id(subscription_id):
    for subscription in subscriptions_list:
        if subscription["id"] == subscription_id:
            return jsonify(subscription), 200
    return jsonify({"error": "Subscription not found"}), 404

@app.route("/subscriptions/<int:subscription_id>", methods=["PUT"])
def update_subscriptions(subscription_id):
    data = request.get_json()
    for subscription in subscriptions_list:
        if subscription["id"] == subscription_id:
            subscription["email"] = data.get("email",subscription["email"])
            subscription["name"] = data.get("name",subscription["name"])
            subscription["plan"] = data.get("plan",subscription["plan"])
            return jsonify(subscription), 200
    return jsonify({"error": "Subscription not found"}), 404    

if __name__ == "__main__":
    app.run(debug=True)