class MockIo:

    def __init__(self, player_inputs=[]):
        self.player_inputs = player_inputs

    def get_player_input(self):
        return self.player_inputs.pop(0)

    def print_message(self, message):
        self.message = message

    def is_empty(self):
        return len(self.player_inputs) == 0

    def mock_user_input(self, input):
        self.player_inputs.append(input)
