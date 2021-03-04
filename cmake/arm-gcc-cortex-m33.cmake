# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

set(MCPU_FLAGS "-mthumb -mcpu=cortex-m33+nodsp+nofp")
set(VFP_FLAGS "-mfloat-abi=softfp")

include(${CMAKE_CURRENT_LIST_DIR}/arm-gcc-cortex-toolchain.cmake)
