import math
from core_tic_tac_toe.player import Player


class HardComputerPlayer(Player):
    def __init__(self, name, symbol, opponent_symbol, board, game_logic):
        super().__init__(name=name, symbol=symbol, board=board)
        self.__opponent_symbol = opponent_symbol
        self.__game_logic = game_logic

    @property
    def opponent_symbol(self):
        return self.__opponent_symbol

    @property
    def game_logic(self):
        return self.__game_logic

    def make_move(self):
        best_score = -math.inf
        best_move = None

        available_moves = self.board.get_available_positions()

        for move in available_moves:
            self.board.execute_move(move - 1, self.symbol)
            score = self.minimax(0, False)
            self.board.undo_execution(move)

            if score > best_score:
                best_score = score
                best_move = move

        self.board.execute_move(best_move - 1, self.symbol)

    def minimax(self, depth, is_maximizer):
        board_state = self.board.get_board()
        available_moves = self.board.get_available_positions()

        if self.game_logic.check_winner(board_state, self.symbol):
            return 10 - depth
        elif self.game_logic.check_winner(board_state, self.opponent_symbol):
            return -10 + depth
        elif len(available_moves) == 0:
            return 0

        current_player_symbol = self.__get_current_player(is_maximizer)
        best_score = None
        for move in available_moves:
            self.board.execute_move(move - 1, current_player_symbol)
            score = self.minimax(depth + 1, not is_maximizer)
            self.board.undo_execution(move)

            best_score = self.__get_score(best_score, score, is_maximizer)

        return best_score

    def __get_current_player(self, is_maximizer):
        if is_maximizer:
            return self.symbol
        else:
            return self.opponent_symbol

    def __get_score(self, best_score, score, is_maximizer):
        if best_score is None:
            return score
        elif is_maximizer:
            return max(best_score, score)
        else:
            return min(best_score, score)
