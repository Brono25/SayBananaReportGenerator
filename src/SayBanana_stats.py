from utils.user_stats import UserStats
import sys

def load_user_productions_content(file: str):
    content = []
    with open(file, "r") as file:  
        for line in file.readlines():
            content.append(line.rstrip())
    return content


def generate_user_report(user_productions: str, output_pdf: str):
    """
    Generates a user report based on daily statistics from the SayBanana app.

    Parameters:
    - user_productions (str): Path to a .txt file with daily user stats, stored in SayBanana Firebase storage.
    - output_pdf (str): File path where the generated PDF report will be saved.
    """
    content = load_user_productions_content(user_productions)
    user_stats = UserStats(content)
    user_stats.create_pdf_report(output_pdf)


if __name__ == "__main__":

    generate_user_report("test/user_productions.txt", "output/test1.pdf")
    generate_user_report("test/user_productions-2.txt", "output/test2.pdf")
