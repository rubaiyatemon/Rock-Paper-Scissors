from RPS_game import play, quincy, mrugesh, kris, abbey
from RPS import player

# Example of playing 1000 games against each bot
if __name__ == "__main__":
    print("Playing against Quincy:")
    win_rate_quincy = play(player, quincy, 1000, verbose=True)
    print(f"Win rate against Quincy: {win_rate_quincy}%")

    print("\nPlaying against Mrugesh:")
    win_rate_mrugesh = play(player, mrugesh, 1000, verbose=True)
    print(f"Win rate against Mrugesh: {win_rate_mrugesh}%")

    print("\nPlaying against Abbey:")
    win_rate_abbey = play(player, abbey, 1000, verbose=True)
    print(f"Win rate against Abbey: {win_rate_abbey}%")

    print("\nPlaying against Kris:")
    win_rate_kris = play(player, kris, 1000, verbose=True)
    print(f"Win rate against Kris: {win_rate_kris}%")
