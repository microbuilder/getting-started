---
page_type: sample
description: Using the Arm MPS3 AN524 with Azure RTOS
languages:
- c
products:
- azure-rtos
---

# Getting started with the Arm MPS3 FGPA board and the AN524

**Total completion time**:  30 minutes

In this tutorial you use Azure RTOS on the AN524, which is an Arm Cortex-M33
image that can be run on the MPS3 FPGA prototyping board.

## Prerequisites

* [Git](https://git-scm.com/downloads) for cloning the repository
* Hardware

    > * The [Arm MPS3 FPGA Prototyping Board](https://developer.arm.com/tools-and-software/development-boards/fpga-prototyping-boards/mps3) (MPS3)
    > * The [AN524 SSE-200 FPGA image for MPS3](https://developer.arm.com/tools-and-software/development-boards/fpga-prototyping-boards/download-fpga-images)

## Building the Sample

> This has only been tested on OS X, where `rebuild.sh` has been modified
  to call `greadlink` since OS X's native `readlink` isn't compatible with
  the standard Linux version. If building on Linux, change the script to
  use `readlink` instead.
  
```bash
$ cd ARM/MPS3_AN524
$ tools/rebuild.sh
```

