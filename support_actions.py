class SupportActions:
    def track(self):
        return "Please provide your order ID."

    def refund(self):
        return "Refunds take 5–7 business days."

    def payment(self):
        return "We accept cards, PayPal, and EFT."

class SupportBot:
    def __init__(self):
        actions = SupportActions()
        self.actions = {
            "track": actions.track,
            "refund": actions.refund,
            "payment": actions.payment
        }

    def respond(self, user_input):
        action = self.actions.get(user_input, self.default_response)
        return action()

    def default_response(self):
        return "Sorry, I didn’t understand."
