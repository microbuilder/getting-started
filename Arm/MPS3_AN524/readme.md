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
image that can be run on the MPS3 FPGA prototyping board or in QEMU.

## Prerequisites

* [Git](https://git-scm.com/downloads) for cloning the repository
* Hardware

    > * The [Arm MPS3 FPGA Prototyping Board](https://developer.arm.com/tools-and-software/development-boards/fpga-prototyping-boards/mps3) (MPS3)
    > * The [AN524 SSE-200 FPGA image for MPS3](https://developer.arm.com/tools-and-software/development-boards/fpga-prototyping-boards/download-fpga-images)

## System Setup

### FTDI VCP Drivers

Your OS may not properly enumerate the four serial ports provided by an FTDI
USB serial chip on the MPS3 board. If they don't appear, you must install the
latest VCP driver and restart your system:
https://ftdichip.com/drivers/vcp-drivers/

You should see five distinct serial ports (one for the LPC1768 debug MCU, and
four from the FTDI chip), where the first two ports from the FTDI chip are of
relevance to this demo:

- `tty.usbserial-xxxxxxxxA` = The MPS3 bootloader
- `tty.usbserial-xxxxxxxxB` = Azure (etc.) serial output

### AN524 PyOCD Support

If you wish to debug, MPS3 AN524 support is available in pyocd via a CMSIS
pack, which can be installed as follows:

```bash
$ pyocd pack -u
$ pyocd pack -i SSE-200-MPS3
$ pyocd list --targets | grep MPS3
```

You can then start a GDB debug session via:

```bash
$ pyocd gdbserver --target=sse-200-mps3
```

Then in another terminal:

```bash
$ gdb
(gdb) target remote localhost:3333
...
```

> Please note that there is a known issue with resetting the AN524 with the
  debugger (https://github.com/pyocd/pyOCD/issues/1078). The `pyocd_user.py`
  script in this `Arm/MPS3_AN524` folder provides a workaround for this issue,
  and pyocd should be run from the folder where this script is located.

## Building the Sample

> This has only been tested on OS X, where `rebuild.sh` has been modified
  to call `greadlink` since OS X's native `readlink` isn't compatible with
  the standard Linux version. If building on Linux, change the script to
  use `readlink` instead.
  
```bash
$ cd ARM/MPS3_AN524
$ tools/rebuild.sh
```
