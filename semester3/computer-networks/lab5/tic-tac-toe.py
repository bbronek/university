import socket


def find_move(board):
    return next((index for index, occupied in enumerate(board) if not occupied), None)


def play(host, port, name):
    if not name.strip() or any(character in name for character in "\r\n"):
        raise ValueError("Enter a nonempty, single-line player name")
    board = [False] * 25
    with socket.create_connection((host, port)) as connection:
        with connection.makefile("r", encoding="utf-8") as responses:
            for line in responses:
                message = line.strip()
                print(message)
                if message.startswith("WELCOME"):
                    connection.sendall(f"LOGIN {name}\n".encode())
                elif message == "NEW GAME":
                    board = [False] * 25
                elif message.startswith("OPPONENT "):
                    location = int(message.split()[1])
                    if not 0 <= location < len(board):
                        raise ValueError("Invalid opponent move")
                    board[location] = True
                elif message == "YOUR_TURN":
                    move = find_move(board)
                    if move is None:
                        raise ValueError("The server requested a move on a full board")
                    board[move] = True
                    connection.sendall(f"MOVE {move}\n".encode())
                elif message in {"SUCCESS", "FAILED"}:
                    return message
                elif message == "ERROR":
                    raise RuntimeError("The server rejected the previous command")
    raise ConnectionError("The server disconnected before the match ended")


if __name__ == "__main__":
    play(input("Host: "), int(input("Port: ")), input("Player name: "))
