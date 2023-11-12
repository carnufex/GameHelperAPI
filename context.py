context = {
    'pause': False,
    'healing': {
        'potions': {
            'hp': {
                'enabled': False,
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
              "hpPc": 60,
              "mpPc": 20,
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
                "hotkey": "f1",
                "mpPc": 20,
                "spell": "utani hur"
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
