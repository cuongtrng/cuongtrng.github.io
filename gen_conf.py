import yaml
from datetime import datetime


def parse_deadline(conf):
    return datetime.strptime(f'{conf["year"]} {conf["deadline"]}', "%Y %b. %d")


def format_date(date_str, year):
    """
    Supports:
    - 'Apr 1' → 'Apr. 1'
    - 'Dec 7-13' → 'Dec. 7-13'
    """
    if "-" in date_str:
        # handle range (e.g., "Dec 7-13")
        month, days = date_str.split()
        start_day, end_day = days.split("-")

        start = datetime.strptime(f"{year} {month} {start_day}", "%Y %b. %d")

        # format month once + range
        month_fmt = start.strftime("%b.")
        return f"{month_fmt} {int(start_day)}-{int(end_day)}"

    else:
        # single date
        date_obj = datetime.strptime(f"{year} {date_str}", "%Y %b. %d")
        return date_obj.strftime("%b. %-d")


def days_left(deadline_date):
    today = datetime.today()
    delta = (deadline_date - today).days

    if delta < 0:
        return '{{<span style="color:red">passed</span>}}'
    elif delta <= 7:
        return '{{<span style="color:red">' + f'{delta}' + ' days left</span>}}'
    else:
        return f"{delta} days left"


def read_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["conferences"]


def generate_jemdoc(conferences, filename="conferences.jemdoc"):
    conferences.sort(key=parse_deadline)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# jemdoc: menu{MENU}{conferences.html}\n")
        f.write("= Conferences Tracker\n\n")

        now = datetime.now().strftime("%b. %-d, %Y")
        f.write(f"- *Last updated:* {now}\n")

        f.write("~~~\n")
        f.write("{}{table}{confs}\n")
        f.write("Name | DT | Deadline | Date | Location ||\n")

        for i, conf in enumerate(conferences):
            deadline_date = parse_deadline(conf)
            dt_status = days_left(deadline_date)

            # formatted dates
            deadline_fmt = format_date(conf["deadline"], conf["year"])
            notif_fmt = format_date(conf["date"], conf["year"])

            name_with_link = f'[{conf["link"]} {conf["name"]}]'

            row = (
                f'{name_with_link} | {dt_status} | {deadline_fmt} | '
                f'{notif_fmt} | {conf["location"]}'
            )

            if i < len(conferences) - 1:
                row += " ||"

            f.write(row + "\n")

        f.write("~~~\n\n")



# ===== Run =====
if __name__ == "__main__":
    conferences = read_yaml("database.yml")
    generate_jemdoc(conferences, filename="jemdoc_files/conferences.jemdoc")
