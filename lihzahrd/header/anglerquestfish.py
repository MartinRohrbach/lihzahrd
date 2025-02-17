import enum


class AnglerQuestFish(enum.IntEnum):
    BATFISH = 0
    BUMBLEBEE_TUNA = 1
    CATFISH = 2
    CLOUDFISH = 3
    CURSEDFISH = 4
    DIRTFISH = 5
    DYNAMITE_FISH = 6
    EATER_OF_PLANKTON = 7
    FALLEN_STARFISH = 8
    THE_FISH_OF_CTHULHU = 9
    FISHOTRON = 10
    HARPYFISH = 11
    HUNGERFISH = 12
    ICHORFISH = 13
    JEWELFISH = 14
    MIRAGE_FISH = 15
    MUTANT_FLINXFIN = 16
    PENGFISH = 17
    PIXIEFISH = 18
    SPIDERFISH = 19
    TUNDRA_TROUT = 20
    UNICORN_FISH = 21
    GUIDE_VOODOO_FISH = 22
    WYVERNTAIL = 23
    ZOMBIE_FISH = 24
    AMANITIA_FUNGIFIN = 25
    ANGELFISH = 26
    BLOODY_MANOWAR = 27
    BONEFISH = 28
    BUNNYFISH = 29
    CAPN_TUNABEARD = 30
    CLOWNFISH = 31
    DEMONIC_HELLFISH = 32
    DERPFISH = 33
    FISHRON = 34
    INFECTED_SCABBARDFISH = 35
    MUDFISH = 36
    SLIMEFISH = 37
    TROPICAL_BARRACUDA = 38

    # none of the other tools know what fish this is ... *shrug*
    UNKNOWN1 = 39

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"
