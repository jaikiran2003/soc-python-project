from dataclasses import dataclass, field

from app.game_logic import (
    check_bingo,
    generate_board,
    get_winning_square_ids,
    toggle_square,
)
from app.models import BingoLine, BingoSquareData, GameMode, GameState


@dataclass
class GameSession:
    """Holds the state for a single game session."""

    game_state: GameState = GameState.START
    game_mode: GameMode = GameMode.BINGO
    board: list[BingoSquareData] = field(default_factory=list)
    winning_line: BingoLine | None = None
    show_bingo_modal: bool = False

    @property
    def winning_square_ids(self) -> set[int]:
        return get_winning_square_ids(self.winning_line)

    @property
    def progress_percentage(self) -> int:
        if not self.board:
            return 0
        marked = sum(1 for sq in self.board if sq.is_marked and not sq.is_free_space)
        total = sum(1 for sq in self.board if not sq.is_free_space)
        return int((marked / total) * 100) if total > 0 else 0

    @property
    def has_bingo(self) -> bool:
        return self.game_state == GameState.BINGO

    def start_game(self, mode: GameMode = GameMode.BINGO) -> None:
        self.game_mode = mode
        self.board = generate_board(mode)
        self.winning_line = None
        self.game_state = GameState.PLAYING
        self.show_bingo_modal = False

    def handle_square_click(self, square_id: int) -> None:
        if self.game_state != GameState.PLAYING:
            return
        self.board = toggle_square(self.board, square_id)

        if self.winning_line is None:
            bingo = check_bingo(self.board)
            if bingo is not None:
                self.winning_line = bingo
                self.game_state = GameState.BINGO
                self.show_bingo_modal = True

    def reset_game(self) -> None:
        self.game_state = GameState.START
        self.board = []
        self.winning_line = None
        self.show_bingo_modal = False

    def dismiss_modal(self) -> None:
        self.show_bingo_modal = False
        self.game_state = GameState.PLAYING


# In-memory session store keyed by session ID
_sessions: dict[str, GameSession] = {}


def get_session(session_id: str) -> GameSession:
    """Get or create a game session for the given session ID."""
    if session_id not in _sessions:
        _sessions[session_id] = GameSession()
    return _sessions[session_id]
