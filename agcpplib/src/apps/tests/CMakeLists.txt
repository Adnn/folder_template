project(tests VERSION "${CMAKE_PROJECT_VERSION}")

set(${PROJECT_NAME}_HEADERS
    catch.hpp
)

set(${PROJECT_NAME}_SOURCES
    main.cpp
)

add_executable(${PROJECT_NAME}
               ${${PROJECT_NAME}_HEADERS}
               ${${PROJECT_NAME}_SOURCES}
)

#target_link_libraries(${PROJECT_NAME}
#    PRIVATE
#        ag::)

set_target_properties(${PROJECT_NAME} PROPERTIES
                      VERSION "${${PROJECT_NAME}_VERSION}"
)

install(TARGETS ${PROJECT_NAME})
