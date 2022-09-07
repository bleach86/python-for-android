from pythonforandroid.recipe import BootstrapNDKRecipe


class LibSDL2Image(BootstrapNDKRecipe):
    version = '2.6.2'
    url = 'https://github.com/libsdl-org/SDL_image/releases/download/release-{version}/SDL2_image-{version}.tar.gz'
    dir_name = 'SDL2_image'

    # patches = ['extra_cflags.patch']

    def get_recipe_env(self, arch=None, with_flags_in_cc=True, with_python=False):
        env = super().get_recipe_env(arch, with_flags_in_cc, with_python)
        env['SUPPORT_JPG'] = True
        env['SUPPORT_PNG'] = True
        env['SUPPORT_WEBP'] = True


recipe = LibSDL2Image()
