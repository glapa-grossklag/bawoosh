import subprocess
import config
import sys
import os
import logging


# ------------------------------------------------------------------------------
# Shell Builtins
# ------------------------------------------------------------------------------


def my_help(args):
    # For at least a few of these builtin commands, the args aren't actually used,
    # but including them in the signature allows for easier use in a dictionary.
    print("Builtins:")
    for elem in builtins:
        print("\t" + elem)


builtins = {
    "exit": lambda args: sys.exit(int(args[0])),
    "cd": lambda args: os.chdir(args[0]),
    "help": my_help
}


# ------------------------------------------------------------------------------
# Workers
# ------------------------------------------------------------------------------


def execute(command: list[str]) -> None:
    # head     tail
    #  |         |
    #  |    _____|_____
    #  v   /           \
    # echo Hello, world!
    head = command[0]
    tail = command[1:]

    if head in builtins:
        builtins[head](tail)
    else:
        subprocess.run(command)


def main() -> None:
    while True:
        line = input(config.prompt)
        line = line.strip()

        # Comments
        if line.startswith("#"):
            continue

        # Handle ';'s
        commands = line.split(";")

        for command in commands:
            try:
                execute(command.split())
            except Exception as e:
                print(e, file=sys.stderr)


if __name__ == "__main__":
    main()
