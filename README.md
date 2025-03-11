
<br>

# CineBot

Intelligent movie recommendation chatbot that leverages NLP techniques to provide relevant movie suggestions based on user queries.

<br>

## Features

- **Natural Language Processing (NLP):** Uses embeddings and transformer-based models to understand user queries.
- **Similarity Matching:** Utilizes cosine similarity to find the most relevant movies.
- **Movie Recommendation:** Suggests movies based on genre and user preferences.

<br>

## Technologies used

- **[Python](https://www.python.org/)**: Core programming language for backend logic and machine learning.
- **[Transformers](https://huggingface.co/docs/transformers/index)**: Provides pre-trained language models for NLP tasks.
- **[Sentence-Transformers](https://www.sbert.net/)**: Generates embeddings for semantic similarity calculations.

<br>

## Install and configuration

*Clone the repository :*
```
git clone https://github.com/yourusername/CineBot.git
cd CineBot
```

*Create a virtual environment :*
```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

*Install dependencies :*
```
pip install -r requirements.txt
```

*Download necessary NLP models :*
```
python -m spacy download fr_core_news_md
```

<br>

## How to run
*Once the project configuration is completed you can execute :*
```
python main.py
```

<br>

## Features to come

- Possibility to select your movie theater.
- Possibility to change date and time of day.
- Web interface (Django).
- Movies's ratings in results.

<br>

## Contact
Feel free to [mail me](mailto:mas.ste@gmail.com) for any questions, comments, or suggestions.
