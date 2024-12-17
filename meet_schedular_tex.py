from datetime import datetime, timedelta
import  csv

def input_collect():
    with open('meet_details.txt', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        fieldnames = next(reader)
        data = [row for row in reader]
    slots = {fieldname: [row[i] for row in data] for i, fieldname in enumerate(fieldnames)}
    return slots

slots = input_collect()
for i in range(len(slots['duration'])):
    slots['duration'][i] = timedelta(hours=int(slots['duration'][i].split(':')[0]), minutes=int(slots['duration'][i].split(':')[1]))
# Initial time


initial_time = datetime.strptime("2:30 PM", "%I:%M %p")  # 8:00 AM

# Cumulative time calculation
cumulative_times = []
current_time = initial_time

for i in range(len(slots['duration'])):
    cumulative_times.append(current_time)
    current_time += slots['duration'][i]
cumulative_times.append(current_time)

print(r"""\documentclass[12pt]{article}
\usepackage[T1]{fontenc}
\usepackage{inter}
\renewcommand*\familydefault{\sfdefault}
\usepackage{arydshln}
\usepackage{geometry}
\usepackage{multirow}
\setlength{\arrayrulewidth}{0.5mm}
\setlength{\tabcolsep}{10pt}
\renewcommand{\arraystretch}{1.5}

\geometry{
a4paper,
top=2cm,
bottom=1in,
left=1.5cm,
right=1.5cm
}
\begin{document}
\begin{center}
    \fontsize{30}{30}\selectfont\intermedium Climate Group Meeting (CGM) \\ \bigskip
\end{center}
\hline
\vspace{1em}
\textbf{Venue:} NAC II conference room.\\
\textbf{Date:} December 23 2024.\\
\\
\textbf{Meeting chair:} Sanket
\vspace{0.5em}\\
\begin{center}
    \begin{tabular}{ |p{4.5cm}|p{2cm}|p{5.5cm}|p{3cm}|  }
 \hline
\textbf{Time Slot} & \textbf{Duration} & \textbf{Title} & \textbf{Speaker} \\
\hline""")

# Print the results
for i in range(len(cumulative_times)-1):
    print(f"{cumulative_times[i].strftime('%I:%M %p')} - {cumulative_times[i+1].strftime('%I:%M %p')} & {slots['duration'][i]} & {slots['title'][i]} & {slots['name'][i]}\\\\")

print(r"""\hline
\end{tabular}
\end{center}
\vspace{1em}
\textbf{Session chair:}
To ensure a smooth and informative session, please maintain the schedule.
\\
\textbf{Presenter:}
Kindly adhere to the scheduled time frame. 
\end{document}""")
