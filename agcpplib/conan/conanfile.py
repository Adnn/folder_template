from conans import ConanFile, CMake, tools

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
        "build_tests": [True, False],
        "shared": [True, False],
        "visibility": ["default", "hidden"],
    }
    default_options = {
        "build_tests": False,
        "shared": False,
        "visibility": "hidden"
    }

    #requires = ()

    build_requires = ("cmake/3.17.3@ag/stable",)

    build_policy = "missing"
    generators = "cmake_paths", "cmake"
    revision_mode = "scm"

    scm = {
        "type": "git",
        # Not using auto url: Azure CI clones via https, so auto exported recipe would use https
        "url": "git@bitbucket.org:agdevs/{{project}}.git",
        "revision": "auto",
        "submodule": "recursive",
    }


    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_tests"] = self.options.build_tests
        cmake.definitions["CMAKE_CXX_VISIBILITY_PRESET"] = self.options.visibility
        cmake.definitions["CMAKE_PROJECT_{{Project}}_INCLUDE"] = \
            path.join(self.source_folder, "cmake", "conan", "customconan.cmake")
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
