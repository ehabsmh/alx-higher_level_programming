#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    args = sys.argv
    args_len = len(args)

    print(f"{args_len - 1} argument{'s' if args_len - 1 != 1 else ''}",
          end='')

    print(f"{'.' if args_len - 1 == 0 else ':'}")

    for i in range(1, args_len):
        print(f"{i}: {args[i]}")
