# Function with outputs
def format_name(f_name: str, l_name: str) -> str:
    formatted_f_name: str = f_name.title()
    formatted_l_name: str = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("JuLiE", "KoHl"))
