import customtkinter as ctk
import pandas as pd
from sentiment_analyzer import analyze_sentiment
from tkinter import filedialog, messagebox

class SentimentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Sentiment Analyzer")
        self.root.geometry("800x600")

        # Set appearance mode and default color theme
        ctk.set_appearance_mode("Dark") # Dark mode
        ctk.set_default_color_theme("green") # We'll override this with purple/black later

        # Custom colors for purple and black theme
        self.primary_purple = "#8A2BE2" # Blue Violet
        self.dark_purple = "#4B0082" # Indigo
        self.text_color = "#E0E0E0" # Light Grey
        self.background_color = "#1A1A1A" # Very Dark Grey/Near Black
        self.accent_color = "#FFD700" # Gold for highlights if needed

        self.root.configure(fg_color=self.background_color) # Set root window background

        # Header Frame
        self.header_frame = ctk.CTkFrame(master=root, fg_color=self.dark_purple, corner_radius=10)
        self.header_frame.pack(pady=20, padx=20, fill="x")

        self.title_label = ctk.CTkLabel(master=self.header_frame, text="Social Media Sentiment Analysis",
                                        font=("Arial", 28, "bold"), text_color=self.text_color)
        self.title_label.pack(pady=10)

        # Input Frame
        self.input_frame = ctk.CTkFrame(master=root, fg_color=self.background_color, corner_radius=10, border_color=self.primary_purple, border_width=2)
        self.input_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.input_label = ctk.CTkLabel(master=self.input_frame, text="Enter Social Media Post:",
                                        font=("Arial", 16), text_color=self.text_color)
        self.input_label.pack(pady=(20, 5), padx=10, anchor="w")

        self.text_input = ctk.CTkTextbox(master=self.input_frame, width=500, height=80,
                                        font=("Arial", 14), text_color=self.text_color,
                                        fg_color="#333333", border_color=self.primary_purple, border_width=1,
                                        wrap="word")
        self.text_input.pack(pady=5, padx=10, fill="x")

        self.analyze_button = ctk.CTkButton(master=self.input_frame, text="Analyze Single Post",
                                            command=self.analyze_single_post,
                                            fg_color=self.primary_purple, hover_color=self.dark_purple,
                                            text_color_disabled=self.text_color,
                                            font=("Arial", 16, "bold"))
        self.analyze_button.pack(pady=10, padx=10)

        # File Input
        self.file_label = ctk.CTkLabel(master=self.input_frame, text="Or Analyze from CSV File (with 'text' column):",
                                       font=("Arial", 16), text_color=self.text_color)
        self.file_label.pack(pady=(20, 5), padx=10, anchor="w")

        self.file_path_entry = ctk.CTkEntry(master=self.input_frame, placeholder_text="No file selected",
                                            width=400, font=("Arial", 14), text_color=self.text_color,
                                            fg_color="#333333", border_color=self.primary_purple, border_width=1)
        self.file_path_entry.pack(pady=5, padx=10, side="left", expand=True, fill="x")

        self.browse_button = ctk.CTkButton(master=self.input_frame, text="Browse CSV",
                                           command=self.browse_file,
                                           fg_color=self.primary_purple, hover_color=self.dark_purple,
                                           font=("Arial", 16, "bold"))
        self.browse_button.pack(pady=5, padx=(0, 10), side="left")

        self.analyze_file_button = ctk.CTkButton(master=self.input_frame, text="Analyze CSV",
                                                 command=self.analyze_csv_file,
                                                 fg_color=self.primary_purple, hover_color=self.dark_purple,
                                                 font=("Arial", 16, "bold"))
        self.analyze_file_button.pack(pady=5, padx=10, side="left")


        # Result Frame
        self.result_frame = ctk.CTkFrame(master=root, fg_color=self.background_color, corner_radius=10, border_color=self.primary_purple, border_width=2)
        self.result_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.result_label = ctk.CTkLabel(master=self.result_frame, text="Analysis Result:",
                                         font=("Arial", 16), text_color=self.text_color)
        self.result_label.pack(pady=(20, 5), padx=10, anchor="w")

        self.result_text = ctk.CTkTextbox(master=self.result_frame, width=500, height=150,
                                         font=("Arial", 14), text_color=self.text_color,
                                         fg_color="#333333", border_color=self.primary_purple, border_width=1,
                                         wrap="word", state="disabled") # Disabled for display only
        self.result_text.pack(pady=5, padx=10, fill="both", expand=True)

    def analyze_single_post(self):
        text = self.text_input.get("1.0", "end-1c").strip()
        if not text:
            messagebox.showwarning("Input Error", "Please enter some text to analyze.")
            return

        sentiment = analyze_sentiment(text)
        self.display_result(f"Input: '{text}'\nSentiment: {sentiment}")

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.file_path_entry.delete(0, ctk.END)
            self.file_path_entry.insert(0, file_path)

    def analyze_csv_file(self):
        file_path = self.file_path_entry.get()
        if not file_path:
            messagebox.showwarning("File Error", "Please select a CSV file first.")
            return

        try:
            df = pd.read_csv(file_path)
            if 'text' not in df.columns:
                messagebox.showerror("File Error", "CSV must contain a column named 'text'.")
                return

            results = []
            for index, row in df.iterrows():
                text = str(row['text'])
                sentiment = analyze_sentiment(text)
                results.append(f"Text: '{text}'\nSentiment: {sentiment}\n---")

            self.display_result("\n".join(results))

        except FileNotFoundError:
            messagebox.showerror("File Error", "The specified file was not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_result(self, message):
        self.result_text.configure(state="normal") # Enable to insert text
        self.result_text.delete("1.0", "end")
        self.result_text.insert("1.0", message)
        self.result_text.configure(state="disabled") # Disable after insertion

if __name__ == "__main__":
    root = ctk.CTk()
    app = SentimentApp(root)
    root.mainloop()