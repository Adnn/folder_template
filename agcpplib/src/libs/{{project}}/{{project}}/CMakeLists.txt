project({{project}} VERSION "${CMAKE_PROJECT_VERSION}")

set(${PROJECT_NAME}_HEADERS
)

set(${PROJECT_NAME}_SOURCES
)

cmc_find_dependencies()

add_library(${PROJECT_NAME}
            ${${PROJECT_NAME}_SOURCES}
            ${${PROJECT_NAME}_HEADERS}
)

add_library(ag::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

cmc_target_current_include_directory(${PROJECT_NAME})

#target_link_libraries(${PROJECT_NAME}
#    PUBLIC
#)

set_target_properties(${PROJECT_NAME} PROPERTIES
                      VERSION "${${PROJECT_NAME}_VERSION}"
)


##
## Install
##

install(TARGETS ${PROJECT_NAME} EXPORT ${PROJECT_NAME}Targets)

include(cmc-install)
# Install the headers preserving the directory hierarchy
cmc_install_with_folders(FILES ${${PROJECT_NAME}_HEADERS}
                         DESTINATION include/${PROJECT_NAME}/${PROJECT_NAME}
)
cmc_install_packageconfig(${PROJECT_NAME} ${PROJECT_NAME}Targets
                          #DEPENDS_COMPONENTS ${_internal_dependencies_public}
                          FIND_FILE "CMakeFinds.cmake.in"
                          NAMESPACE ag::
)
