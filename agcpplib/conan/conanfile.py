from conans import ConanFile, CMake, errors, tools

from os import path


class {{Project}}Conan(ConanFile):
    """ Conan recipe for {{Project}} """

    name = "{{project}}"
    license = "property of AstuteGraphics"
    url = "https://bitbucket.org/agdevs/{{project}}"
    description = "{{Project_description}}"
    #topics = ("", "", ...)
    settings = ("os", "compiler", "build_type", "arch")
    options = {
        "shared": [True, False],
        "build_tests": [True, False],
        "visibility": ["default", "hidden"],
    }
    default_options = {
        "shared": False,
        "build_tests": False,
        "visibility": "default"
    }

    #requires = ()

    build_requires = ("cmake_installer/[>=3.16]@conan/stable",)

    build_policy = "missing"
    generators = "cmake_paths", "cmake"

    scm = {
        "type": "git",
        "subfolder": "cloned_repo",
        # Not using auto forurl: Azure CI clones via https, so auto exported recipe would use https
        "url": "git@bitbucket.org:agdevs/{{project}}.git",
        "revision": "auto",
        "submodule": "recursive",
    }


    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_CXX_VISIBILITY_PRESET"] = self.options.visibility
        cmake.definitions["CMAKE_PROJECT_{{Project}}_INCLUDE"] = \
            path.join(self.source_folder, "cmake", "conan", "customconan.cmake")
        cmake.definitions["BUILD_tests"] = self.options.build_tests
        cmake.configure()
        return cmake


    def build(self):
        cmake = self._configure_cmake()
        cmake.build()


    def package(self):
        cmake = self._configure_cmake()
        cmake.install()


    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
