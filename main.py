import tkinter as tk
from tkinter import simpledialog,messagebox

def generate_fixtures(teams):
    fixtures = []
    if len(teams)%2!=0:
        teams.append('BYE')

    num_days=len(teams) - 1
    half = len(teams) // 2

    for day in range(num_days):
        day_fixtures = []
        for i in range(half):
            home=teams[i]
            away=teams[-i-1]
            day_fixtures.append(f'{home} - {away}')

        fixtures.append(day_fixtures)
        teams.insert(1,teams.pop())

        return fixtures

def on_generate():
    if len(team_list) < 2:
       messagebox.showerror('Input Error',"Please Add at least 2 teams!")
       return

    fixtures = generate_fixtures(team_list)

    result_text.delete(1.0,tk.END)
    for day, matches in enumerate(fixtures):
        result_text.insert(tk.END, f'Day {day+1}:\n')
        for match in matches:
            result_text.insert(tk.END,f'{match}\n')
        result_text.insert(tk.END, "\n")


def add_team():
        team_name = simpledialog.askstring("AddTeam","Enter a team name: ")
        if team_name:
            team_list.append(team_name)
            update_team_display()

def update_team_display():
    team_display.delete(0, tk.END)
    for team in team_list:
        team_display.insert(tk.END, team)

def clear_teams():
    team_list.clear()
    update_team_display()

root = tk.Tk()
root.title("Fixtures Generator")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

team_list = []

add_team_button = tk.Button(root, text="Add Team", command=add_team)
add_team_button.grid(row=0,column=0,padx=10,pady=10)

team_display = tk.Listbox(root,height=6,width=30)
team_display.grid(row=1,column=0,padx=10,pady=10)

clear_button = tk.Button(root,text="Clear Teams", command=clear_teams)
clear_button.grid(row=2,column=0,padx=10,pady=10)

generate_button = tk.Button(root, text="Generate Fixtures", command=on_generate)
generate_button.grid(row=3,column=0,padx=10,pady=10)

result_text = tk.Text(root,width=40,height=15)
result_text.grid(row=0,column=1,rowspan=4,padx=10,pady=10)

root.mainloop()