# Install dependencies
#!pip install sumy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text, num_sentences=3):
    """Summarizes input text using Latent Semantic Analysis (LSA)"""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)

    return "\n".join([str(sentence) for sentence in summary])

# Example Usage
input_text = """
Natural Language Processing (NLP) is a field of Artificial Intelligence focused on enabling computers to understand, process, and generate human language. 
It involves multiple tasks such as text summarization, sentiment analysis, and machine translation. 
Summarization techniques extract key points from a document to generate a concise representation of its content.
"""
print("Summary:")
print(summarize_text(input_text))
