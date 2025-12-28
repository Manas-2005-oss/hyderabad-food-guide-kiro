def load_context():
    with open("product.md", "r", encoding="utf-8") as file:
        return file.read()

context = load_context()

print("🍽️ Hyderabad Street Food Local Guide")
print("Powered by custom local context\n")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Goodbye!")
        break

    response = "Based on Hyderabad local food context:\n"

    if "spicy" in user_input:
        response += (
            "- Pani Puri near Charminar (very spicy and tangy)\n"
            "- Haleem in Old City (rich and spicy, especially during Ramzan)"
        )

    elif "pani" in user_input:
        response += "Try Pani Puri near Charminar. It is spicy and tangy."

    elif "haleem" in user_input:
        response += "Haleem is popular during Ramzan, especially in the Old City."

    elif "chai" in user_input:
        response += "Irani Chai with Osmania biscuits is famous at Nimrah Café."

    elif "pizza" in user_input:
        response += "Sorry, this item is not part of Hyderabad street food context."

    else:
        response += "Please ask about Hyderabad street food listed in the guide."

    print("Guide:", response)
