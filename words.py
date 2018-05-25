from talon.voice import Context, Key

ctx = Context('words')

keymap = {
    'dot company': '.com',

    'state command': 'cmd',
    'state control': 'ctrl',
    'state option': 'opt',
    'state static': 'static ',

    'word cycling': 'cyclom',
    'word define': 'def ',
    'word doctor': 'docker',
    'word for each': 'forEach',
    'word import': 'import ',
    'word get': 'git',
    'word gist': 'gist',
    'word hero': 'heroku',
    'word jason': 'JSON',
    'word no': 'null',
    'word no super': 'NULL',
    'word printf': 'printf',
    'word slack': 'slack',
    'word string': 'JSON.stringify',
    'word them': 'vim',
    'word will': 'twilio',
    'word with': 'width',
}

ctx.keymap(keymap)
