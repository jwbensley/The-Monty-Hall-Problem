#!/usr/bin/python3


import argparse
import os
import random
import sys


"""
This function plays one full game (choose a door, then the option of a
subsequent change, $switches).
The door which is revealed is chosen at random if rand_reveal==True.
"""
def play_game(rand_reveal=False, switches=False, verbose=False):

    doors = {1, 2, 3}
    first_choice = random.randint(1, 3)
    doors.discard(first_choice)

    """"
    If revealing a door at random, choose of the two doors the contestant
    has chosen. The winning door may also be the same door which is revelaed.
    """
    if rand_reveal:
        revealed_door = list(doors)[random.randint(0, 1)]
        winning_door = random.randint(1, 3)
        doors.discard(winning_door)
    # Else, if not revealing a random door, ensure it is not the winning door.
    else:
        winning_door = random.randint(1, 3)
        doors.discard(winning_door)
        revealed_door = list(doors)[0]

    # The host has revealed the winning door by chance, ending the game
    if revealed_door == winning_door:
        result = False
        switch_fail = False
        revealed = True
        return result, revealed, switch_fail
    else:
        revealed = False

    if switches:
        doors = {1, 2, 3}
        doors.discard(first_choice)
        doors.discard(revealed_door)
        second_choice = list(doors)[0]

    if switches and (winning_door == second_choice):
        result = True
        switch_fail = False
    elif not switches and (winning_door == first_choice):
        result = True
        switch_fail = False
    elif switches and (winning_door == first_choice):
        result = False
        switch_fail = True
    else:
        result = False
        switch_fail = False

    if verbose:
        print("Prize is behind door: {}".format(winning_door))
        print("Player chose door: {}".format(first_choice))
        print("Monty opens door: {}".format(revealed_door))
        if switches:
            print("Player switched to door: {}".format(second_choice))
        else:
            print("Player remains with door: {}".format(first_choice))
        if result:
            print("Player wins!")
        else:
            print("Player loses!")
        print("")

    return result, revealed, switch_fail


def simulate(num_games, rand_reveal, switches, verbose):

    results = []
    reveals = []
    switch_fails = []

    for i in range(0, num_games):
        result, revealed, switch_fail = play_game(
            rand_reveal, switches, verbose
        )
        results.append(result)
        reveals.append(revealed)
        switch_fails.append(switch_fail)

    """
    result_counts keys will be alphabetical,
    Flase is the first key, then True
    """
    result_counts = {x: results.count(x) for x in set(results)}
    reveal_counts = {x: reveals.count(x) for x in set(reveals)}
    switch_counts = {x: switch_fails.count(x) for x in set(switch_fails)}

    """
    If simulating a small number of games the player may have won or lost
    100% of them so add the missing dict keys:
    """
    if True not in reveal_counts:
        reveal_counts[True] = 0
    if False not in result_counts:
        result_counts[False] = 0
    if True not in result_counts:
        result_counts[True] = 0
    if True not in switch_counts:
        switch_counts[True] = 0

    if switches:
        print(
            "Player lost (original choice was correct) for {:.2f}% ({}/{}) "
            "games".format(
                (switch_counts[True] / num_games) * 100,
                switch_counts[True],
                num_games,
            )
        )
        if rand_reveal:
            print(
                "\t->Host accidently revealed winning door for {:.2f}% "
                "({}/{}) games".format(
                    (reveal_counts[True] / num_games) * 100,
                    reveal_counts[True],
                    num_games,
                )
            )
        print(
            "Player won (original choice was incorrect) for {:.2f}% ({}/{}) "
            "games".format(
                (result_counts[True] / num_games) * 100,
                result_counts[True],
                num_games,
            )
        )
    else:
        print(
            "Player lost (original choice was incorrect) for {:.2f}% ({}/{}) "
            "games".format(
                (result_counts[False] / num_games) * 100,
                result_counts[False],
                num_games,
            )
        )
        if rand_reveal:
            print(
                "\t->Host accidently revealed winning door for {:.2f}% "
                "({}/{}) games".format(
                    (reveal_counts[True] / num_games) * 100,
                    reveal_counts[True],
                    num_games,
                )
            )
        print(
            "Player won (original choice was correct) for {:.2f}% ({}/{}) games".format(
                (result_counts[True] / num_games) * 100,
                result_counts[True],
                num_games,
            )
        )
    print("")


def parse_args():

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--num", type=int, default=10000)
    parser.add_argument("--verbose", default=False, action="store_true")

    return vars(parser.parse_args())


def main():

    args = parse_args()
    random.seed()

    print("")
    print("Results when a known losing door is revealed by the host:")
    print("Player does not switch door")
    simulate(args["num"], False, False, args["verbose"])
    print("Player switches door")
    simulate(args["num"], False, True, args["verbose"])

    print("")
    print("Results when a random door is revealed by the host:")
    print("Player does not switch door")
    simulate(args["num"], True, False, args["verbose"])
    print("Player switches door")
    simulate(args["num"], True, True, args["verbose"])


if __name__ == "__main__":
    sys.exit(main())
