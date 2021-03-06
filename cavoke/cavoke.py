import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.displayName = "Cavoke"
        self.description = "A Platform for creating and hosting multiplayer turn-based board games"
        self.webpage = "https://cavoke.wlko.me"
        self.svnTargets["master"] = "https://github.com/cavoke-project/cavoke.git|master"
        self.svnTargets["develop"] = "https://github.com/cavoke-project/cavoke.git|develop"
        self.defaultTarget = "develop"

    def setDependencies(self):
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtdeclarative"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = None
        self.runtimeDependencies["libs/qt5/qtnetworkauth"] = None
        self.runtimeDependencies["kde/frameworks/tier1/karchive"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        self.subinfo.options.configure.args += ["-DBUILD_ALL=OFF", "-DBUILD_CLIENT=ON", "-DQT_MAJOR_VERSION=5"]
        
    @property
    def applicationExecutable(self):
        return os.environ.get('ApplicationExecutable', 'cavoke_client')
        
    def createPackage(self):
        self.defines["appname"] = self.applicationExecutable
        self.defines["apppath"] = "Applications/Cavoke/" + self.defines["appname"] + ".app"
        self.defines["company"] = "Cavoke Team"
        self.defines["icon"] = os.path.join(self.sourceDir(), "client", "resources", "packaging", "cavoke.ico")
        self.defines["shortcuts"] = [{"name" : self.subinfo.displayName, "target": f"bin/{self.applicationExecutable}.exe"}]
        
        return super().createPackage()
