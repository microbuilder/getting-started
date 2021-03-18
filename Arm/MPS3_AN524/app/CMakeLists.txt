# Copyright (c) 2021 Linaro Limited.
# Licensed under the MIT License.

set(LINKER_SCRIPT "${CMAKE_CURRENT_LIST_DIR}/startup/mps3_an524.ld")

set(SOURCES
    startup/startup_cmsdk_mps3_an524_bl2.S
    main.c
    board_init.c
    console.c
)

add_executable(${PROJECT_NAME} ${SOURCES})

target_link_libraries(${PROJECT_NAME} 
    PUBLIC
        azrtos::threadx

        # app_common
        # jsmn
        AN524
        tfm_api
        # netx_driver
)

target_link_options(${PROJECT_NAME}
    PRIVATE 
        -T${LINKER_SCRIPT} -Wl,-Map=${PROJECT_NAME}.map)

set_target_properties(${PROJECT_NAME}
    PROPERTIES 
        LINK_DEPENDS ${LINKER_SCRIPT}
        SUFFIX ".elf"
)

target_include_directories(${PROJECT_NAME} 
    PUBLIC 
        .
)

trusted_firmware_build(BINARY_DIR ${CMAKE_BINARY_DIR}/tfm
                       BOARD mps3/an524
                       IPC
                       ISOLATION_LEVEL 1
                       BL2
                       ENABLED_PARTITIONS TFM_PARTITION_PLATFORM TFM_PARTITION_CRYPTO)
