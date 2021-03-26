import os
import glob

client_mods = ["AmbientSounds", "BetterAdvancements", "BetterFoliage", "BetterFps", "BetterPlacement", "Blur",
               "ChatCopier", "ChatFlow", "classicbar", "clearwater", "ClientTweaks", "ColouredTooltips", "Controlling",
               "CTM-MC", "CustomBackgrounds", "CustomLoadingScreen", "CustomMainMenu", "CustomSkinLoader_Forge",
               "DynamicSurroundings", "DynamicSurroundingsHuds", "dynamistics", "EntityCulling", "fluidict", "FpsReducer",
               "FullscreenWindowed", "gendustryjei", "hiddenarmor", "ikwid", "InGameAccountSwitcher", "InGameInfoXML",
               "InventoryHud", "InvMove", "InvMove", "itlt", "jeibees", "jeiintegration", "jeivillagers", "jepb",
               "JEROreIntegration", "jetif", "just-enough-brewcraft", "just-enough-harvestcraft", "JustEnoughCharacters",
               "JustEnoughEnergistics", "JustEnoughReactors", "JustEnoughResources", "lesslag", "LoadingScreens",
               "lootcapacitortooltips", "MAGE", "MainMenuScale", "memorycleaner", "MenuMobs", "MineMenu", "MoBends",
               "modnametooltip", "Modpack Configuration Checker", "MouseTweaks", "NonUpdate", "OldJavaWarning",
               "PackModeMenu", "particleculling", "potiondescriptions", "ProportionalDestructionParticles",
               "RealFirstPerson2", "ResourceLoader", "scalingguis", "ScreenshotToClipboard", "shapeselector",
               "ShoulderSurfing", "shutupmodelloader", "SmoothFont", "soundsystemreloader", "SplashAnimation",
               "StuffASockInIt", "tc6aspects4jei", "ThaumicJEI", "TieredTooltips", "tinkersjei", "Tips", "Toast Control",
               "Unifine", "WHAT", "WorldSelectionAdvanced"]

count = 0

for cmodIndex in range(len(client_mods)):
    cmodString = client_mods[cmodIndex] + '*.jar'
    filesFound = glob.glob(cmodString)

    if len(filesFound) >= 1:
        os.remove(filesFound[0])
        print("Deleted " + cmodString)
        count += 1
    else:
        print("Did not find " + cmodString)
print("Finished deleting client mods. Deleted " + str(count) + " mods!")
