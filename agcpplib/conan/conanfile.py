from conans import ConanFile, CMake, errors, tools

from os import path


class {{Project}}Conan(ConanFile):
    """ Conan recipe for {{Project}} """

    name = "{{project}}"
    license = "property of AstuteGraphics"
    url = "https://bitbucket.org/agdevs/{{project}}"
    description = "{{Project_description}}"
    #topics = ("", "", ...)
    settings = (
        "os", # Naturally forwarded for native compilation
        "compiler", # Build-helper sets -> CONAN_COMPILER
                    # Need to check it manually in CMake scripts (check_compiler_version)
                    # * compiler.cppstd -> CONAN_CMAKE_CXX_STANDARD & CONAN_CMAKE_CXX_EXTENSIONS (standard with "gnu" prefix, e.g. "gnu14")
                    #   Need to map it manually to CMAKE_CXX_STANDARD && CMAKE_CXX_EXTENSIONS (conan_set_std)
                    # * compiler.libcxx -> CONAN_LIBCXX
                    #   Need to map it manually to compiler dependent flags (conan_set_libcxx)
                    # * compiler.runtime -> CONAN_LINK_RUNTIME
                    #   Need to manually alter the compilation flags (conan_set_vs_runtime)
        "build_type", # Buildhelper auto sets CMake var CMAKE_BUILD_TYPE
                      # All that is needed
        "arch") # Naturally forwarded for native compilation
    options = {
        "shared": [True, False], # Buildhelper auto sets CMake var BUILD_SHARED_LIBS
                                 # All that is needed
        "build_tests": [True, False], # Need to manually map to CMake var BUILD_tests
    }
    default_options = {
        "shared": False,
        "build_tests": False,
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
