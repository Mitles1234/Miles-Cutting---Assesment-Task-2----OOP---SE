class Weapons:
    def __init__(self, name, wptype, level, damage, wtrdmg, firdmg, natdmg):
        self.name = name
        self.wptype = wptype
        self.level = level
        self.damage = damage
        self.wtrdmg = wtrdmg
        self.firdmg = firdmg
        self.natdmg = natdmg
    # Weapon(Crayon, Shortsword, 14, 8, 1.2, 0.9, 1)

class Armour:
    def __init__(self, name, artype, level, protection, wtrpro, firpro, natpro):
        self.name = name
        self.artype = artype
        self.level = level
        self.protection = protection
        self.wtrpro = wtrpro
        self.firpro = firpro
        self.natpro = natpro
    # Armour(Iron Armour, Helmet, 3, 5, 1, 1, 1)

    def get_artype():
        return self.artype
    