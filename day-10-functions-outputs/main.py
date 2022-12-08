# Function with outputs
# def format_name(f_name: str, l_name: str) -> str:
#     formatted_f_name: str = f_name.title()
#     formatted_l_name: str = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"
#
#
# print(format_name("JuLiE", "KoHl"))

# Multiple return values
def format_name(f_name: str, l_name: str) -> str:
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."

    formatted_f_name: str = f_name.title()
    formatted_l_name: str = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))
