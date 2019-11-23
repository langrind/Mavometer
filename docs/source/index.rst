
The Mavometer
=============

**Mavometer** is a GUI app that displays MAVLink connection information and
statistics.

It can operate on a live connection (e.g. the stream mirrored by
`Mission Planner <http://ardupilot.org/planner/>`_) or it can read a file.

It provides connection-level information, such as protocol version, and
message information, such as data rate by message type.

It is not a protocol analyzer - it does not display individual message
contents. It is not a ground station - it does not read or display telemetry
values from MAVLink messages.

It is written in Python, and should run on any OS that supports PyQt5
and pymavlink.

Get started at the `Python Package Index page <https://pypi.org/project/Mavometer/>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   cmdline_args

