pyquark
=========

## Installation

Run below command to install pyquark module:

    python setup.py install

## Architecture

+----------------------------------------------+
|                    example                   |
|          +-----------------------------------+
|          | +---------------------------------+
|          | |       arduino                   |
+----------+ +---------------------------------+
+----------------------------------------------+
|                         +------+             |
|                         | Gpio |             |
|                         +---+--+             |
|                             ^                |
|                             | inherits       |
|                     +-------+------+         |
|                     |              |         |
|                     |              |         |
|     +-------+  +----+----+   +-----+-----+   |
|     |  Aio  |  |   Dio   |   |   PwmIO   |   |
|     +---+---+  +--+------+   +-----+-----+   |
|         |         |                |         |
| depends +---------+                | depends |
|         |                          |         |
|         v                          v         |
|    +----+------+   depends   +-----+-----+   |
|    |  GpioPin  | <---------+ |   PwmPin  |   |
|    +-----------+             +-----------+   |
|                                              |
+----------------------------------------------+

## Reference
- https://github.com/intel-iot-devkit/mraa
- https://github.com/galileo-chofrock/pyGalileo