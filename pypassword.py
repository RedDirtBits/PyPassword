import string
import random
import secrets
import PySimpleGUI as sg


class GenPassword:
    def __init__(self, password_length: int):

        self.password_length = password_length
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.numbers = string.digits
        self.punctuations = string.punctuation

    def create_password(self):

        random_choices = {
            0: self.lowercase,
            1: self.uppercase,
            2: self.numbers,
            3: self.punctuations,
        }

        password = []

        for _ in range(self.password_length):

            secret_num = secrets.choice(range(len(random_choices)))

            password.extend(list(random_choices[secret_num]))

        return "".join(random.sample(password, self.password_length))


# Add the GUI with PySimpleGUI

sg.theme("DarkGrey9")

pass_length = [
    [
        sg.Text(
            "Enter Password Length:", size=(25, 0), font=("Courier New", 10, "bold")
        ),
        sg.InputText(
            "",
            size=(10, 0),
            font=("Courier New", 10, "bold"),
            key="password_length",
            enable_events=True,
        ),
    ]
]

output = [
    [
        sg.Multiline(
            size=(60, 2),
            font=("Courier New", 9),
            key="output",
            write_only=True,
            no_scrollbar=True,
            text_color="white",
        )
    ]
]

layout = [
    [pass_length],
    [sg.Text("")],
    [sg.Frame("Password", output)],
    [sg.Button("Generate", key="GENERATE"), sg.Text("", size=(40, 1)), sg.Exit()],
]

# Can add the option margins=(x, y) here instead of maunally entering within the elements or layout
window = sg.Window("Password Generator", layout, grab_anywhere=False)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    if event == "password_length" and values["password_length"]:
        try:
            number_test = int(values["password_length"])
        except:
            window["password_length"].update(values["password_length"][:-1])

    if event == "GENERATE":
        try:
            get_password = GenPassword(int(values["password_length"])).create_password()
            window["output"].update(get_password)
        except ValueError:
            window["output"].update("You must specify a password length")

window.close()


# test1 = GenPassword(25).create_password()
# print(test1)
