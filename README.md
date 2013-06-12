# serialenum

## Introduction

Serialenum is a simple utility to correctly enumerate all available and present
serial ports on a given system. There are a number of ways to enumerate serial
ports, but they are platform-specific and vary in effectiveness. Serialenum
attempts to provide the best possible methods for each supported platform.

## Installation

    pip install serialenum

## Usage

    import serialenum

    serialenum.enumerate()

The `enumerate` method will return a list of serial ports or a blank list, if
none are found. If serial ports could not be enumerated, it will return `None`.

### Using command line script

Script called serialenum can be used from command line

    serialenum

It prints out all found serial ports, one per line.

## Supported Platforms

1. Windows XP or later
2. Recent Linux 2.6+ kernels

## Windows

The Windows implementation iterates over a registry key to ensure that
usb-to-serial converters and oddly-named COM ports are discovered. This should
work correctly on any modern version of Windows.

## Linux

The Linux implementation uses `/dev/serial` to enumerate attached serialenum
port devices. This avoids the fake `ttyS` devices typically present and also
accounts for usb-to-serial converters.

## TODO

* Add fallback support for older Linux systems
* Add support for more operating systems (testing help needed)
