import tkinter as tk
from tkinter import messagebox


RIDDLES = [
	("What is the middle of Paris?", "R"),
	("Which word is spelt wrong in every dictionary?", "Wrong"),
	("What can you catch but not throw?", "Cold"),
	("What animal can run the fastest—an elephant, squirrel or a mouse?", "Elephant"),
	(
		"I am an odd number, but if you take away just a single letter I become even. "
		"Can you guess my number?",
		"Seven",
	),
	("I'm tall when I'm young, and I'm short when I'm old, what am I?", "Candle"),
	("What is so fragile that saying its name breaks it?", "Silence"),
	("What has four eyes but can't see?", "Mississippi"),
	("Where can you find cities, towns, shops, and streets but no people?", "Map"),
	("What has a neck but no head?", "Bottle"),
]


class Riddler(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Riddler on the Roof")
		self.geometry("620x360")
		self.minsize(500, 300)
		self.configure(bg="#202938")
		self.index = 0
		self.score = 0

		tk.Label(
			self, text="Riddler on the Roof", font=("Segoe UI", 26, "bold"),
			fg="#f4c95d", bg="#202938"
		).pack(pady=(24, 4))
		self.progress = tk.Label(self, bg="#202938", fg="#b8c3d1", font=("Segoe UI", 11))
		self.progress.pack()
		self.question = tk.Label(
			self, bg="#202938", fg="white", wraplength=540,
			justify="center", font=("Segoe UI", 16)
		)
		self.question.pack(pady=28)
		self.answer = tk.Entry(self, font=("Segoe UI", 14), justify="center", width=30)
		self.answer.pack(ipady=7)
		self.answer.bind("<Return>", lambda event: self.check_answer())
		self.button = tk.Button(
			self, text="Check answer", command=self.check_answer,
			bg="#f4c95d", fg="#202938", activebackground="#ffe49a",
			relief="flat", font=("Segoe UI", 11, "bold"), padx=18, pady=8
		)
		self.button.pack(pady=20)
		self.load_question()

	def load_question(self):
		self.progress.config(text=f"Riddle {self.index + 1} of {len(RIDDLES)}  •  Score: {self.score}")
		self.question.config(text=RIDDLES[self.index][0])
		self.answer.delete(0, tk.END)
		self.answer.focus_set()

	def check_answer(self):
		guess = self.answer.get().strip().casefold()
		if not guess:
			return
		if guess == RIDDLES[self.index][1].casefold():
			self.score += 1
			messagebox.showinfo("Correct!", "Nice work!")
		else:
			messagebox.showinfo("Not quite", f"The answer is {RIDDLES[self.index][1]}.")
		self.index += 1
		if self.index == len(RIDDLES):
			messagebox.showinfo("Finished", f"You scored {self.score} out of {len(RIDDLES)}.")
			self.index = 0
			self.score = 0
		self.load_question()


if __name__ == "__main__":
	Riddler().mainloop()
