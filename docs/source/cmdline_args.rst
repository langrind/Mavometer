======================
Command Line Arguments
======================

You can provide any command line option that is valid for Qt,
for example if you are running on a Windows platform you could
provide ``-style windowsvista``.

You can provide any command line option that is valid for the
underlying windowing system used by Qt. For example, if you are
running on X Windows, ``--display :0``.

Most of the command line options processed directly by **Mavometer**
have to do with setting up the MAVLink protocol source. Here all
the options currently supported:

+-----------------------+-------------------------------------------------------------+
| ``--help``            | Print usage message                                         |
+-----------------------+-------------------------------------------------------------+
| ``--mavlink-port``    | Device, file or network address from which to read MAVLink  |
+-----------------------+-------------------------------------------------------------+
| ``--mavlink-dialect`` | Set MAVLink dialect to any installed pymavlink dialect      |
+-----------------------+-------------------------------------------------------------+
| ``--mavlink-version`` | Set MAVLink version to 1.0 or 2.0                           |
+-----------------------+-------------------------------------------------------------+


Examples of ``--mavlink-port``:

+-----------------------------------------+-------------------------------------------+
| ``--mavlink-port /dev/ttyACM0``         | Direct USB connection on Linux            |
+-----------------------------------------+-------------------------------------------+
| ``--mavlink-port /dev/ttyUSB0,57600``   | USB connected FTDI UART at 57.6 Kbits/s   |
+-----------------------------------------+-------------------------------------------+
| ``--mavlink-port test.tlog``            | Read from file ``test.tlog``              |
+-----------------------------------------+-------------------------------------------+
| ``--mavlink-port tcp:127.0.0.1:14551``  | TCP connection                            |
+-----------------------------------------+-------------------------------------------+

Examples of ``--mavlink-dialect``:

+-----------------------------------------+-------------------------------------------+
| ``--mavlink-dialect ardupilotmega``     | Use dialect ArduPilotMega                 |
+-----------------------------------------+-------------------------------------------+
