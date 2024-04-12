################################################################################
#
# pygpio
#
################################################################################
PYGPIO_VERSION = 0.1
PYGPIO_SOURCE = "https://codeload.github.com/mikolaj-t/python-buildroot-gpio/tar.gz/$(PYGPIO_VERSION)"
PYGPIO_DEPENDENCIES = gpiozero
PYGPIO_SETUP_TYPE = setuptools

$(eval $(python-package))