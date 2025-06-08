print("Hey there! I’m CryptoBuddy 🤖 Let’s explore some smart, green crypto picks!")
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

user_query = input("Ask me about crypto: ").lower()

if "sustainable" in user_query:
    recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
    print(f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

elif "trending" in user_query or "rising" in user_query:
    rising_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
    print(f"The following cryptos are trending up: {', '.join(rising_coins)} 🚀")

elif "long-term" in user_query or "growth" in user_query:
    options = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
    if options:
        print(f"{options[0]} is a solid long-term option! 📈")
    else:
        print("Cardano is a smart long-term bet based on sustainability and trend. 🚀")

else:
    print("I’m still learning! Try asking about sustainability or trends. 🧠")

profitable = [coin for coin, data in crypto_db.items()
              if data["price_trend"] == "rising" and data["market_cap"] == "high"]



sustainable = [coin for coin, data in crypto_db.items()
               if data["energy_use"] == "low" and data["sustainability_score"] > 0.7]



print("⚠️ Reminder: Crypto is risky—always do your own research!")
