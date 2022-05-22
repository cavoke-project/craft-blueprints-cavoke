import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.displayName = "Cavoke"
        self.description = "A really solid software package that does nifty things"
        self.webpage = "https://cavoke.wlko.me"
        self.svnTargets["master"] = "https://github.com/cavoke-project/cavoke.git|master"
        self.svnTargets["develop"] = "https://github.com/cavoke-project/cavoke.git|develop"
        self.defaultTarget = "develop"

    def setDependencies(self):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtdeclarative"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols"] = None
        self.runtimeDependencies["libs/qt5/qtnetworkauth"] = None
        self.runtimeDependencies["kde/frameworks/tier1/karchive"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.args += ["-DBUILD_ALL=OFF", "-DBUILD_CLIENT=ON", "-DQT_MAJOR_VERSION=5"]