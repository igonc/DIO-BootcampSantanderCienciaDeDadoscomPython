def show_poem(date, *args, **kwargs):
    poem = '\n'.join(args)
    meta_data = '\n'.join([f'{key.title()}: {value}' for key, value in kwargs.items()])
    message = f'{date}\n\n{poem}\n\n{meta_data}'
    print(message)

show_poem(
    'Friday, October 7, 2022',
    'She Walks in Beauty',
    'She walks in beauty, like the night',
    'Of cloudless climes and starry skies;',
    'And all that’s best of dark and bright',
    'Meet in her aspect and her eyes;',
    'Thus mellowed to that tender light',
    'Which heaven to gaudy day denies.',
    'One shade the more, one ray the less',
    'Had half impaired the nameless grace',
    'Which waves in every raven tress,',
    'Or softly lightens o’er her face;',
    'Where thoughts serenely sweet express,',
    'How pure, how dear their dwelling-place.',
    'And on that cheek, and o’er that brow,',
    'So soft, so calm, yet eloquent,',
    'The smiles that win, the tints that glow,',
    'But tell of days in goodness spent,',
    'A mind at peace with all below,',
    'A heart whose love is innocent.',
    author='Lord Byron',
    year='1803',
)