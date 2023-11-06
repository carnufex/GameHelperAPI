context = {
    'pause': False,
    'healing': {
        'potions': {
            'hp': {
                'enabled': True,
                'hotkey': 'f9',
                'hpPc': 30,
            },
            'mp': {
                'enabled': True,
                'hotkey': 'f6',
                'mpPc': 70
            },
        },
        'spells': {
            "criticalHealing": {
              "enabled": True,
              "hotkey": "f3",
              "hpPc": 100,
              "mpPc": 20,
              "spell": "exura san"
            },
            "lightHealing": {
              "enabled": True,
              "hotkey": "f2",
              "hpPc": 80,
              "mpPc": 10,
              "spell": "exura gran"
            }
        }
    },
    'lastUsed': {
        'heal': 0,
        'pot': 0,
        'utility': 0
    },
    'player': {
        'hp': None,
        'hpPc': None,
        'mp': None,
        'mpPc': None,
        'isParalyzed': None
    },
    'screenshot': None
}
