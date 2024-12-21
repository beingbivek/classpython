number = int(
    input(
        "Enter a number: "
    )
)

if number % 2 == 0:
    if number % 5 == 0:
        print(
            f"The number {number} is divisible by both 2 and 5."
        )
    else:
        print(
            f"The number {number} is divisible by only 2."
        )
else:
    print(
        f"The number {number} is not divisible by 2."
    )

        