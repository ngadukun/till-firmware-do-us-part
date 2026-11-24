"""Till Firmware Do Us Part.

A wedding vow to a device, ruined by one update, printed to stdout.
Deterministic, standard library only, writes no files.
"""

LINE = (
    "I promised to love you through every update, but this firmware "
    "changed you — and now I don't recognise the device I married."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
