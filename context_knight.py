from src.gameplay.core.tasks.orchestrator import TasksOrchestrator


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
                'mpPc': 60
            },
        },
        'spells': {
            "criticalHealing": {
              "enabled": False,
              "hotkey": "shift+f3",
              "hpPc": 50,
              "mpPc": 20,
              "spell": "exura gran san"
            },
            "mediumHealing": {
              "enabled": False,
              "hotkey": "f3",
              "hpPc": 60,
              "mpPc": 10,
              "spell": "exura san"
            },
            "lightHealing": {
              "enabled": True,
              "hotkey": "f2",
              "hpPc": 80,
              "mpPc": 15,
              "spell": "exura gran"
            },
            "paralyze": {
                "enabled": True,
                "hotkey": "f2",
                "mpPc": 15,
                "spell": "exura ico"
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
    'orchestrators': {
        'healing': TasksOrchestrator(),
        'item': TasksOrchestrator(),
    },




    'map': {
        'coordinate': None,
        'previousCoordinate': None,
        'lastCoordinateVisited': None,
    },
}
