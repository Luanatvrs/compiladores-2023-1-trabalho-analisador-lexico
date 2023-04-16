import re
from enum import Enum
from dataclasses import dataclass

class TokenClass(Enum):
    PR = r"(struct\b|if\b|int\b|else\b|while\b|for\b|\bfloat\b|double\b|char\b|break\b|case\b|void\b|return)"
    CN = r"(\d+(\.\d*)?|\.\d+)(?![a-zA-Z])"
    ID = r"([a-zA-Z_][a-zA-Z0-9_]*|main|printf)"
    CT = r'\".*?\"'  
    OP = r"(==|!=|<=|>=|\|\||&&|\+=|-=|\*=|\=|--|\+\+|\+|\/|->|\*|\-|\||!|&|%|<|>)"
    DL = r"\[|\]|\(|\)|\{|\}|\;|\,|\:"

class Token:

    def __init__(self, token_class, value, token_id):
        self.token_class = token_class
        self.token_value = value
        self.token_id = token_id

    def __str__(self) -> str:
        return f'< Token id: {self.token_id}, class: {self.token_class.name}, value: {self.token_value} >'
