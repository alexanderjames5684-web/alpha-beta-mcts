import agents.mtcs as mtcs
import game.game as connect



def main():
    game = connect.ConnectFour()
    print("Connect Four starter — Player 1: X, Player 2: O")
    print("Only Horizontal wins are checked. Vertical and Diagonal wins are not checked yet. Enter q to quit.")
    game.display()

    ai = mtcs.MCTS(iterations=1000)


    while game.legal_moves() and not game.check_win():
        try:
            if game.current_player == 1:

                choice = input(f"Player {game.current_player}, choose a column (1-7): ")
            elif game.current_player == 2:
                choice = str(ai.search(game))
        except (EOFError, KeyboardInterrupt):
            print("\nGame closed.")
            return

        if choice.strip().lower() == "q":
            print("Game closed.")
            return

        try:
            # Human column 1 corresponds to internal column 0.
            game.apply_move(int(choice) - 1)
        except ValueError as error:
            if not choice.strip().lstrip("+-").isdigit():
                print("Enter a whole number from 1 to 7, or q to quit.")
            else:
                print(error)
            continue
        game.display()


        
    if game.check_win():
                print(f"Player {game.check_win()} wins!")
                return
    else:
         print("The board is full. This starter does not evaluate wins or draws yet.")


if __name__ == "__main__":
    main()
