import tkinter as tk
import random

# =========================================================
# MEMORY MADNESS - ONE FILE
# =========================================================

# COLORS
BG = "#FFF4C2"
CARD = "#FFFFFF"
YELLOW = "#FFD43B"
ORANGE = "#FF9F1C"
RED = "#FF5C5C"
GREEN = "#45D483"
PURPLE = "#9B6BFF"
DARK = "#392E2E"
GRAY = "#756969"

# DATA
FRUITS = [
    "Apel", "Jeruk", "Pisang", "Mangga", "Anggur",
    "Kiwi", "Durian", "Nanas", "Pepaya", "Stroberi"
]

ANIMALS = [
    "Kucing", "Anjing", "Gajah", "Singa", "Harimau",
    "Zebra", "Panda", "Kuda", "Rusa", "Beruang"
]


# =========================================================
# BUTTON
# =========================================================
# BUTTON
# =========================================================

class GameButton(tk.Button):

    def __init__(self, parent, text, command, color=ORANGE):

        super().__init__(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=DARK,
            activebackground=YELLOW,
            activeforeground=DARK,
            font=("Segoe UI", 14, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=25,
            pady=12
        )

        self.normal_color = color

        self.bind(
            "<Enter>",
            lambda event: self.config(bg=YELLOW)
        )

        self.bind(
            "<Leave>",
            lambda event: self.config(bg=self.normal_color)
        )


# =========================================================
# GAME
# =========================================================

class MemoryMadness:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Memory Madness")
        self.root.geometry("850x700")
        self.root.minsize(750, 620)
        self.root.configure(bg=BG)

        self.category = "Fruit"

        self.words = []
        self.level = 1
        self.score = 0
        self.lives = 3
        self.combo = 0
        self.best_combo = 0

        self.current_index = 0
        self.answer = ""
        self.question_index = 0

        self.timer = 8
        self.after_id = None

        self.option_buttons = []


        self.show_menu()


    # =====================================================
    # BASIC
    # =====================================================

    def clear(self):

        if self.after_id is not None:

            try:
                self.root.after_cancel(
                    self.after_id
                )

            except:
                pass

            self.after_id = None

        for widget in self.root.winfo_children():
            widget.destroy()


    def text(
        self,
        value,
        size=20,
        color=DARK,
        bold=False
    ):

        weight = "bold" if bold else "normal"

        return tk.Label(
            self.root,
            text=value,
            bg=BG,
            fg=color,
            font=("Segoe UI", size, weight)
        )



    # =====================================================
    # MENU
    # =====================================================

    def show_menu(self):

        self.clear()

        self.text(
            "MEMORY MADNESS",
            40,
            ORANGE,
            True
        ).pack(pady=(60, 5))

        self.text(
            "Test your memory!",
            17,
            GRAY
        ).pack(pady=(0, 35))

        card = tk.Frame(
            self.root,
            bg=CARD,
            padx=45,
            pady=30
        )

        card.pack()

        GameButton(
            card,
            "PLAY GAME",
            self.choose_category,
            ORANGE
        ).pack(
            pady=8,
            fill="x"
        )

        GameButton(
            card,
            "SETTINGS",
            self.settings,
            PURPLE
        ).pack(
            pady=8,
            fill="x"
        )

        GameButton(
            card,
            "EXIT",
            self.root.destroy,
            RED
        ).pack(
            pady=8,
            fill="x"
        )

        self.text(
            "🍎   🐱   🍌   🐼   🍓",
            25
        ).pack(pady=35)


    # =====================================================
    # CATEGORY
    # =====================================================

    def choose_category(self):

        self.clear()

        self.text(
            "CHOOSE CATEGORY",
            30,
            ORANGE,
            True
        ).pack(pady=(55, 10))

        self.text(
            "What do you want to memorize?",
            16,
            GRAY
        ).pack(pady=(0, 30))

        GameButton(
            self.root,
            "FRUITS",
            lambda: self.start_game("Fruit"),
            ORANGE
        ).pack(
            pady=10,
            ipadx=40
        )

        GameButton(
            self.root,
            "ANIMALS",
            lambda: self.start_game("Animal"),
            RED
        ).pack(
            pady=10,
            ipadx=40
        )

        GameButton(
            self.root,
            "BACK",
            self.show_menu,
            YELLOW
        ).pack(pady=30)


    # =====================================================
    # START
    # =====================================================

    def start_game(self, category):

        self.category = category
        self.level = 1
        self.score = 0
        self.lives = 3
        self.combo = 0
        self.best_combo = 0



        self.new_level()


    def new_level(self):

        self.clear()


        data = (
            FRUITS
            if self.category == "Fruit"
            else ANIMALS
        )

        amount = self.level

        self.words = random.sample(
            data,
            amount
        )

        self.current_index = 0

        self.show_memory()


    # =====================================================
    # HEADER
    # =====================================================

    def header(self):

        top = tk.Frame(
            self.root,
            bg=BG
        )

        top.pack(
            fill="x",
            padx=35,
            pady=15
        )

        tk.Label(
            top,
            text=f"LEVEL {self.level}/10",
            bg=BG,
            fg=ORANGE,
            font=("Segoe UI", 17, "bold")
        ).pack(side="left")

        tk.Label(
            top,
            text=f"Score: {self.score}",
            bg=BG,
            fg=PURPLE,
            font=("Segoe UI", 17, "bold")
        ).pack(side="right")

        hearts = "♥ " * self.lives

        tk.Label(
            self.root,
            text=hearts,
            bg=BG,
            fg=RED,
            font=("Segoe UI", 20, "bold")
        ).pack()


    # =====================================================
    # MEMORY SCREEN
    # =====================================================

    def show_memory(self):

        self.clear()

        self.header()

        if self.category == "Fruit":
            title = "MEMORIZE THE FRUITS!"

        else:
            title = "MEMORIZE THE ANIMALS!"

        self.text(
            title,
            28,
            DARK,
            True
        ).pack(pady=(30, 5))

        self.text(
            f"Level {self.level}: memorize {self.level} word(s)",
            15,
            GRAY
        ).pack(pady=(0, 25))

        self.word_box = tk.Frame(
            self.root,
            bg=CARD,
            width=450,
            height=160
        )

        self.word_box.pack(pady=10)

        self.word_box.pack_propagate(False)

        self.word_label = tk.Label(
            self.word_box,
            text="",
            bg=CARD,
            fg=ORANGE,
            font=("Segoe UI", 32, "bold")
        )

        self.word_label.pack(expand=True)

        self.counter_label = tk.Label(
            self.root,
            text="",
            bg=BG,
            fg=PURPLE,
            font=("Segoe UI", 16, "bold")
        )

        self.counter_label.pack(pady=20)

        self.show_next_word()


    def show_next_word(self):

        if self.current_index >= len(self.words):

            self.counter_label.config(
                text="Great! Get ready..."
            )

            self.after_id = self.root.after(
                1000,
                self.start_question
            )

            return

        word = self.words[
            self.current_index
        ]

        self.word_label.config(
            text=word
        )

        self.counter_label.config(
            text=f"Word {self.current_index + 1} / {len(self.words)}"
        )

        self.current_index += 1

        self.after_id = self.root.after(
            1200,
            self.show_next_word
        )


    # =====================================================
    # QUESTION
    # =====================================================

    def start_question(self):

        self.clear()

        self.header()

        self.question_index = random.randrange(
            len(self.words)
        )

        self.answer = self.words[
            self.question_index
        ]

        if self.category == "Fruit":
            title = "MEMORY CHECK - FRUITS"

        else:
            title = "MEMORY CHECK - ANIMALS"

        self.text(
            title,
            29,
            ORANGE,
            True
        ).pack(pady=(30, 10))

        self.text(
            f"Apa yang muncul pada urutan ke {self.question_index + 1}?",
            20,
            DARK,
            True
        ).pack(pady=15)

        self.text(
            "Pilih jawaban yang benar:",
            14,
            GRAY
        ).pack(pady=(0, 20))

        self.make_options()

        self.start_countdown()


    # =====================================================
    # OPTIONS
    # =====================================================

    def make_options(self):

        data = (
            FRUITS
            if self.category == "Fruit"
            else ANIMALS
        )

        options = [
            self.answer
        ]

        while len(options) < 4:

            candidate = random.choice(
                data
            )

            if candidate not in options:
                options.append(candidate)

        random.shuffle(options)

        self.option_buttons = []

        for index, option in enumerate(options):

            color = (
                YELLOW
                if index % 2 == 0
                else RED
            )

            button = GameButton(
                self.root,
                f"{index + 1}. {option}",
                lambda value=option:
                self.check_answer(value),
                color
            )

            button.pack(
                pady=5,
                ipadx=45
            )

            self.option_buttons.append(
                button
            )


    # =====================================================
    # TIMER
    # =====================================================

    def start_countdown(self):

        self.timer = 8

        self.timer_label = tk.Label(
            self.root,
            text="",
            bg=BG,
            fg=RED,
            font=("Segoe UI", 16, "bold")
        )

        self.timer_label.pack(
            pady=15
        )

        self.countdown()


    def countdown(self):

        if not self.timer_label.winfo_exists():
            return

        self.timer_label.config(
            text=f"Time: {self.timer}"
        )

        if self.timer <= 3:
            self.play()

        if self.timer <= 0:

            self.disable_options()

            self.answer_timeout()

            return

        self.timer -= 1

        self.after_id = self.root.after(
            1000,
            self.countdown
        )


    # =====================================================
    # ANSWER
    # =====================================================

    def disable_options(self):

        for button in self.option_buttons:

            button.config(
                state="disabled"
            )


    def check_answer(self, choice):

        self.disable_options()

        if self.after_id is not None:

            try:
                self.root.after_cancel(
                    self.after_id
                )

            except:
                pass

            self.after_id = None

        if choice == self.answer:

            self.correct()

        else:

            self.wrong(
                f"Correct answer: {self.answer}"
            )


    def answer_timeout(self):

        self.wrong(
            f"Time's up! Answer: {self.answer}"
        )


    # =====================================================
    # CORRECT
    # =====================================================

    def correct(self):


        self.combo += 1

        if self.combo > self.best_combo:
            self.best_combo = self.combo

        points = 100 + (
            self.combo * 25
        )

        self.score += points

        self.feedback(
            True,
            "CORRECT!",
            f"+{points} points"
        )


    # =====================================================
    # WRONG
    # =====================================================

    def wrong(self, message):

        # Stop background music when player gets it wrong

        self.lives -= 1

        self.combo = 0

        self.feedback(
            False,
            "WRONG!",
            message
        )


    # =====================================================
    # FEEDBACK
    # =====================================================

    def feedback(
        self,
        correct,
        title,
        subtitle
    ):

        color = (
            GREEN
            if correct
            else RED
        )

        self.clear()

        self.header()

        card = tk.Frame(
            self.root,
            bg=CARD,
            padx=50,
            pady=35
        )

        card.pack(pady=70)

        tk.Label(
            card,
            text=title,
            bg=CARD,
            fg=color,
            font=("Segoe UI", 34, "bold")
        ).pack(pady=10)

        tk.Label(
            card,
            text=subtitle,
            bg=CARD,
            fg=DARK,
            font=("Segoe UI", 16, "bold")
        ).pack(pady=10)

        if correct:

            tk.Label(
                card,
                text=f"Combo: {self.combo}",
                bg=CARD,
                fg=PURPLE,
                font=("Segoe UI", 15, "bold")
            ).pack(pady=5)

        else:

            tk.Label(
                card,
                text=f"Lives left: {self.lives}",
                bg=CARD,
                fg=RED,
                font=("Segoe UI", 15, "bold")
            ).pack(pady=5)

        self.after_id = self.root.after(
            1400,
            self.after_answer
        )


    # =====================================================
    # NEXT LEVEL
    # =====================================================

    def after_answer(self):

        if self.lives <= 0:

            self.game_over()

            return

        if self.level >= 10:

            self.win_game()

            return

        self.level += 1



        self.new_level()


    # =====================================================
    # WIN
    # =====================================================

    def win_game(self):

        self.clear()


        self.text(
            "YOU WIN!",
            42,
            ORANGE,
            True
        ).pack(pady=(70, 10))

        self.text(
            "You mastered all 10 levels!",
            18,
            DARK,
            True
        ).pack(pady=10)

        self.result_box()

        GameButton(
            self.root,
            "PLAY AGAIN",
            self.choose_category,
            ORANGE
        ).pack(
            pady=12,
            ipadx=30
        )

        GameButton(
            self.root,
            "MENU",
            self.show_menu,
            YELLOW
        ).pack(
            pady=8,
            ipadx=45
        )


    # =====================================================
    # GAME OVER
    # =====================================================

    def game_over(self):

        self.clear()


        self.text(
            "GAME OVER",
            42,
            RED,
            True
        ).pack(pady=(70, 10))

        self.text(
            "Try again and beat your score!",
            17,
            DARK
        ).pack(pady=10)

        self.result_box()

        GameButton(
            self.root,
            "TRY AGAIN",
            self.choose_category,
            ORANGE
        ).pack(
            pady=12,
            ipadx=30
        )

        GameButton(
            self.root,
            "MENU",
            self.show_menu,
            YELLOW
        ).pack(
            pady=8,
            ipadx=45
        )


    # =====================================================
    # RESULT
    # =====================================================

    def result_box(self):

        box = tk.Frame(
            self.root,
            bg=CARD,
            padx=50,
            pady=25
        )

        box.pack(pady=25)

        stats = [
            f"Score: {self.score}",
            f"Level: {self.level}/10",
            f"Best Combo: {self.best_combo}",
            f"Lives: {self.lives}"
        ]

        for value in stats:

            tk.Label(
                box,
                text=value,
                bg=CARD,
                fg=DARK,
                font=("Segoe UI", 15, "bold")
            ).pack(pady=4)


    # =====================================================
    # SETTINGS
    # =====================================================

    def settings(self):

        self.clear()

        self.text(
            "SETTINGS",
            32,
            PURPLE,
            True
        ).pack(pady=(60, 35))

        GameButton(
            self.root,
            "BACK",
            self.show_menu,
            YELLOW
        ).pack(
            pady=30,
            ipadx=45
        )



# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    app = MemoryMadness()

    app.root.mainloop()