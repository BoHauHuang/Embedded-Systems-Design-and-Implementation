# Embedded-Systems-Design-and-Implementation

## Installation

Dependency:

* xtrlock
* pyserial
* keyboard

```
$ sudo bash ./install.sh
$ sudo pip install .
```

Enable service:

```
$ sudo systemctl enable bt_keyboard_adapter_rpi
$ systemctl enable xtrlock --user
```

## Developing

virtualenv:

```
$ poetry shell
$ poetry install
```
