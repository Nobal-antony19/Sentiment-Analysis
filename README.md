# Sentiment-Analysis
Sentiment analysis to determine the emotional tone behind a piece of text, identifying whether it's positive, negative, or neutral. This technique is valuable for understanding opinions, reactions, and attitudes expressed in customer reviews

follow the steps mentioned to achieve the gui based sentiment anlaysis. this is done on a virtual environment. 

1. First, create a dedicated folder for your project. This helps keep your files organized.

Bash:  (open terminal of where the file exactly is or just type cmd on the file path in the file manager) 

mkdir sentiment_analyzer_app
cd sentiment_analyzer_app

2. Place the Python Files

Save the provided sentiment_analyzer.py and app.py files into the sentiment_analyzer_app directory you just created.

3. Create a Virtual Environment
 Open your terminal or command prompt, navigate to your project directory (sentiment_analyzer_app), and run the following command:

Bash(on terminal)

python -m venv venv

4. Activate the Virtual Environment

You need to activate the virtual environment before installing packages or running your application. The activation command varies slightly depending on your operating system:

On Windows:

Bash

.\venv\Scripts\activate


On macOS/Linux:

Bash

source venv/bin/activate


5. Install Required Libraries

Your application uses customtkinter, pandas, and textblob. Install these libraries using pip while your virtual environment is active:

Bash (on terminal)

pip install customtkinter pandas textblob

6. Run the Application ,Final Step

With the virtual environment activated and all dependencies installed, you can now run the main application file (app.py):

Bash (on terminal)

python app.py

