class MockIo:

    def __init__(self, player_inputs=[]):
        self.player_inputs = player_inputs

    def get_player_input(self):
        return self.player_inputs.pop(0)

    def print_message(self, message):
        self.message = message
