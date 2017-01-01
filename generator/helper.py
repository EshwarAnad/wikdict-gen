from itertools import permutations

supported_langs = [
    'de', 'en', 'fr', 'pl', 'sv', 'es', 'pt', 'fi', 'el', 'ru', 'tr',
]


def make_for_langs(functions, langs, **kwargs):
    """ Executes functions for all given languages

        `langs` can also be "all" to execute on all supported languages.
    """
    if langs == ['all']:
        langs = supported_langs
    for lang in langs:
        for func in functions:
            print(lang, func.__name__)
            func(lang)


def make_for_lang_permutations(functions, langs, **kwargs):
    """ Executes functions for all pairwise combinations of the given langs.

        `langs` can also be "all" to execute on all supported languages.
    """
    if langs == ['all']:
        langs = supported_langs
    assert len(langs) >= 2, 'Need at least two languages'

    for func in functions:
        print('>> ' + func.__name__)
        for from_lang, to_lang in permutations(langs, 2):
            print(from_lang, to_lang)
            func(from_lang, to_lang)