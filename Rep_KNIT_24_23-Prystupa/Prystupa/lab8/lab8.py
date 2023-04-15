# Модуль для обробки та аналізу текстових даних

import re

def count_words(text):
    """Підрахунок слів у тексті"""
    words = re.findall(r'\w+', text)
    return len(words)

def count_chars(text):
    """Підрахунок символів у тексті"""
    return len(text)

def count_sentences(text):
    """Підрахунок речень у тексті"""
    sentences = re.findall(r'[^\s][^.!?]*[.!?]', text)
    return len(sentences)

def count_paragraphs(text):
    """Підрахунок абзаців у тексті"""
    paragraphs = text.split('\n\n')
    return len(paragraphs)

def get_keywords(text, n):
    """Отримання n найчастіших слів у тексті"""
    words = re.findall(r'\w+', text)
    freq_dict = {}
    for word in words:
        if word.lower() not in freq_dict:
            freq_dict[word.lower()] = 1
        else:
            freq_dict[word.lower()] += 1
    sorted_freq_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return [word for word, freq in sorted_freq_dict[:n]]
