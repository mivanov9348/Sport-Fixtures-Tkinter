import tkinter as tk
from tkinter import simpledialog, messagebox,filedialog


# Function to generate round-robin fixtures
def generate_fixtures(teams):
    fixtures = []
    if len(teams) % 2 != 0:  # If odd number of teams, add a dummy team
        teams.append("BYE")

    num_days = len(teams) - 1
    half = len(teams) // 2

    for day in range(num_days):
        day_fixtures = []
        for i in range(half):
            home = teams[i]
            away = teams[-i - 1]
            day_fixtures.append(f"{home} vs {away}")

        fixtures.append(day_fixtures)
        # Rotate teams except the first one
        teams.insert(1, teams.pop())

    return fixtures


# Function to handle button click for generating fixtures
def on_generate():
    if len(team_list) < 2:
        messagebox.showerror("Input Error", "Please add at least 2 teams.")
        return

    fixtures = generate_fixtures(team_list)

    # Display the fixtures
    result_text.delete(1.0, tk.END)  # Clear previous result
    for day, matches in enumerate(fixtures):
        result_text.insert(tk.END, f"Day {day + 1}:\n")
        for match in matches:
            result_text.insert(tk.END, f"{match}\n")
        result_text.insert(tk.END, "\n")


# Function to open a popup to add a team
def add_team():
    team_name = simpledialog.askstring("Add Team", "Enter team name:")
    if team_name:
        team_list.append(team_name)
        update_team_display()


# Function to update team list display
def update_team_display():
    team_display.delete(0, tk.END)  # Clear current list
    for team in team_list:
        team_display.insert(tk.END, team)

def save_fixtures():
    # Save fixtures to a text file
    fixtures = result_text.get(1.0, tk.END).strip()
    if fixtures:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(fixtures)
            messagebox.showinfo("Save", "Fixtures saved successfully!")
    else:
        messagebox.showerror("Save Error", "No fixtures to save!")

# Function to handle clearing team list
def clear_teams():
    team_list.clear()
    update_team_display()


# Create the main window
root = tk.Tk()
root.title("Fixture Generator")
root.configure(bg="#171717")

# List to hold the teams
team_list = []

# Add team button
add_team_button = tk.Button(root, text="Add Team", command=add_team,bg="#ffffff", fg="black")
add_team_button.grid(row=0, column=0, padx=10, pady=10)

# Team list display
team_display = tk.Listbox(root, height=6, width=30,  bg="#ffffff", fg="white")
team_display.grid(row=1, column=0, padx=10, pady=10)

# Clear teams button
clear_button = tk.Button(root, text="Clear Teams", command=clear_teams)
clear_button.grid(row=2, column=0, padx=10, pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate Fixtures", command=on_generate)
generate_button.grid(row=3, column=0, padx=10, pady=10)

#save button
save_button = tk.Button(root, text="Save Fixtures", command=save_fixtures)
save_button.grid(row = 4, column = 1, padx = 9, pady = 9)

# Text area to display the result
result_text = tk.Text(root, width=40, height=15, bg="#ffffff", fg="black")
result_text.grid(row=0, column=1, rowspan=4, padx=0, pady=0)

# Start the GUI loop
root.mainloop()
