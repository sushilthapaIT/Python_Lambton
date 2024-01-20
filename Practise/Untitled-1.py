def calculate_upper_section_score():
    total_score = 0

    for category in range(1, 7):
        while True:
            try:
                score = int(input(f"How many {category}s did you score (1-5)? "))
                if 1 <= score <= 5:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        category_score = score * category
        total_score += category_score

    if total_score >= 63:
        total_score += 35

    print(f"Your subtotal is {total_score}")

    if total_score >= 63:
        print("You earned a bonus")
    else:
        print("You did not earn a bonus")

    print(f"Your total is {total_score}")


calculate_upper_section_score()
