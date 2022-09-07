from pythonforandroid.recipe import BootstrapNDKRecipe


class LibSDL2Mixer(BootstrapNDKRecipe):
    version = '2.6.2'
    url = 'https://github.com/libsdl-org/SDL_mixer/releases/download/release-{version}/SDL2_mixer-{version}.tar.gz'
    dir_name = 'SDL2_mixer'

    # patches = ['toggle_modplug_mikmod_smpeg_ogg.patch']


recipe = LibSDL2Mixer()
