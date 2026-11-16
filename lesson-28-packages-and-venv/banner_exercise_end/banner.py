# Banner Maker - turn text into big ASCII art with the pyfiglet package
# Part 2.1 (do not remove this line)
import pyfiglet


# Part 2.2 (do not remove this line)
def make_banner(text: str, font: str) -> pyfiglet.FigletString:
    return pyfiglet.figlet_format(text, font=font)


# Part 2.3 (do not remove this line)
def main():
    name = input("What's your name? ")
    font = input("Pick a font (slant, banner, bubble, digital): ")
    f = make_banner(f"Hi {name}", font)
    print(f)


if __name__ == "__main__":
    main()
