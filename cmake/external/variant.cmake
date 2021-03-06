SET(VARIANT_RELEASE_VERSION v1.4.0)
SET(VARIANT_SOURCE_DIR ${THIRD_PARTY_DIR}/variant)
SET(VARIANT_INCLUDE_DIR ${THIRD_PARTY_INCLUDE_DIR}/variant)
include(ExternalProject)
ExternalProject_Add(
		variant
		PREFIX ${CMAKE_BINARY_DIR}/variant
		SOURCE_DIR ${VARIANT_SOURCE_DIR}
		GIT_REPOSITORY https://github.com/mpark/variant.git
		GIT_TAG e4e5d8d5b24f8206a1e78b5a8da7c428be77962c
		CONFIGURE_COMMAND ""
		BUILD_COMMAND ""
		INSTALL_COMMAND ${CMAKE_COMMAND} -E copy_if_different ${VARIANT_SOURCE_DIR}/${VARIANT_RELEASE_VERSION}/variant.hpp ${VARIANT_INCLUDE_DIR}/variant.hpp
)

add_dependencies(libshogun variant)
