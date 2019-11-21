# Mavometer

**Mavometer** is a PyQt GUI to display MAVLink Connection Information and
Statistics.

It can operate on a live connection (e.g. the stream mirrored by
[Mission Planner](http://ardupilot.org/planner/)) or it can read a file.

It provides connection-level information, such as protocol version, and
message information, such as data rate by message type.

It is not a protocol analyzer - it does not display individual message
contents. It is not a ground station - it does not read or display telemetry
values from MAVLink messages.

It is written in python, and should run on any OS that supports PyQt5
and pymavlink.

## Getting Started

### Prerequisites

* [pymavlink](https://pypi.org/project/pymavlink/) - MAVLink protocol implementation 
* [PyQt5](https://pypi.org/project/PyQt5/) - Mavometer is based on the Qt version 5 framework
* [UQtie](https://pypi.org/project/uqtie/) - utility package for PyQt5 usage

These can all be installed in the same way:

```bash
pip install pymvalink
pip install pyqt5
pip install uqtie
```

Be aware that the appropriate installation procedure for a package can
vary depending on your OS and other factors.

### Installing Mavometer

Install the package:

```bash
pip install mavometer
```

Or clone from GitHub:

```bash
git clone https://github.com/langrind/mavometer.git
```

and then run the setup script:

```bash
python3 setup.py
```

### Run Mavometer

Say you have a Pixhawk connected to a USB port on your Linux machine:

```
$ mavometer --mavlink-port /dev/ttyACM0
```

Or you have a log file produced by QGroundControl:

```
$ mavometer --mavlink-port '/home/langrind/Documents/QGroundControl/Telemetry/2019-11-19 20-38-03.tlog'
```

## Tests

```
$ mavometer --mavlink-port test/test.tlog
```

*NOTE:* timestamping is not supported yet for replaying from files, so bandwidth and frequency
displays are garbage in this case.

## Deployment

TBS: details about usage in different OS environments

## Contributing

This project is *ad hoc* in nature, so I don't foresee contributions. Nevertheless,
feel free to make a pull request.

## Versioning

Versions are assigned in accordance with [Semantic Versioning](http://semver.org/).
For the versions available, see the [tags on this repository](https://github.com/langrind/mavometer/tags).

## Authors

* **[Nik Langrind](https://github.com/langrind)** - *Sole author*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* I used the **PurpleBooth** [README template](https://github.com/PurpleBooth/a-good-readme-template)
* The [pymavlink](https://github.com/ArduPilot/pymavlink) `tools/mavsummarize.py`program performs a
  similar function to **Mavometer**.
