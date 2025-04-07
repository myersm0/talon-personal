from talon import Context, Module, actions, app

mod = Module()
mod.list("symbol_key", desc="All symbols from the keyboard")
mod.list("punctuation", desc="words for inserting punctuation into text")

ctx = Context()
ctx.matches = "tag: user.my_overrides"

# `punctuation_words` is for words you want available BOTH in dictation and as key names in command mode.
# `symbol_key_words` is for key names that should be available in command mode, but NOT during dictation.
punctuation_words = {
    # TODO: I'm not sure why we need these, I think it has something to do with
    # Dragon. Possibly it has been fixed by later improvements to talon? -rntz
    "`": "`",
    ",": ",",  # <== these things
    "back tick": "`",
    "comma": ",",
    # Workaround for issue with conformer b-series; see #946
    "coma": ",",
    "period": ".",
    "full stop": ".",
    "semicolon": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "exclamation mark": "!",
    "exclamation point": "!",
    "asterisk": "*",
    "hash sign": "#",
    "number sign": "#",
    "percent sign": "%",
    "at sign": "@",
    "and sign": "&",
    "ampersand": "&",
    # Currencies
    "dollar sign": "$",
    "pound sign": "£",
    "hyphen": "-",
    "L paren": "(",
    "left paren": "(",
    "R paren": ")",
    "right paren": ")",
}
symbol_key_words = {
    "dot": ".",
    "point": ".",
    "quotation": '"',
    "question": "?",
    "apostrophe": "'",
    "L square": "[",
    "left square": "[",
    "bracket": "[",
    "left bracket": "[",
    "square": "[",
    "R square": "]",
    "right square": "]",
    "r brack": "]",
    "r bracket": "]",
    "right bracket": "]",
    "slash": "/",
    "backslash": "\\",
    "minus": "-",
    "dash": "-",
    "equals": "=",
    "plus": "+",
    "backtick": "`",
    "tilde": "~",
    "bang": "!",
    "down score": "_",
    "underscore": "_",
    "paren": "(",
    "curly brace": "{",
    "left brace": "{",
    "curly bracket": "{",
    "left curly bracket": "{",
    "r brace": "}",
    "right brace": "}",
    "r curly bracket": "}",
    "right curly bracket": "}",
    "angle": "<",
    "left angle": "<",
    "less than": "<",
    "rangle": ">",
    "R angle": ">",
    "right angle": ">",
    "greater than": ">",
    "star": "*",
    "hash": "#",
    "percent": "%",
    "caret sign": "^",
    "pipe": "|",
    "single quote": "'",
    # Currencies
    "dollar": "$",
    "pound": "£",
}

# make punctuation words also included in {user.symbol_keys}
symbol_key_words.update(punctuation_words)
ctx.lists["self.punctuation"] = punctuation_words
ctx.lists["self.symbol_key"] = symbol_key_words
