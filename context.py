context = {
    'pause': False,
    'healing': {
        'potions': {
            'hp': {
                'enabled': True,
                'hotkey': 'f9',
                'hpPc': 50,
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
              "hotkey": "shift+f3",
              "hpPc": 50,
              "mpPc": 20,
              "spell": "exura gran san"
            },
            "mediumHealing": {
              "enabled": True,
              "hotkey": "f3",
              "hpPc": 60,
              "mpPc": 10,
              "spell": "exura san"
            },
            "lightHealing": {
              "enabled": True,
              "hotkey": "f2",
              "hpPc": 80,
              "mpPc": 10,
              "spell": "exura gran"
            },
            "paralyze": {
                "enabled": True,
                "hotkey": "f12",
                "mpPc": 5,
                "spell": "exura"
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
    'screenshot': None,
    'trigger': {
        'looting': False
    },
    'map': {
        'coordinate': None,
        'previousCoordinate': None,
        'lastCoordinateVisited': None,
    },
}
