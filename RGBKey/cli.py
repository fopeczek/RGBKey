import click
from .rgb_class import RGB

@click.group(invoke_without_command=True)
@click.option("--version", '-v', is_flag=True, type=bool, help="Show version")
def main(version):
    if version:
        print("0.0.1")

@main.command()
def test():
    from openrgb import OpenRGBClient
    from openrgb.utils import DeviceType
    client = OpenRGBClient()
    keyboard = client.get_devices_by_type(DeviceType.KEYBOARD)[0]
    if keyboard:
        print("Keyboard found")

@main.command()
@click.option("--human", "-h", is_flag=False, type=bool, help="Show raw data")
@click.argument("keys", type=str)
@click.argument("color", type=str)
def set(human, keys, color):
    from openrgb import OpenRGBClient
    from openrgb.utils import DeviceType, RGBColor
    client = OpenRGBClient()
    keyboard = client.get_devices_by_type(DeviceType.KEYBOARD)[0]
    color = RGB.FromString(color)
    color = RGBColor(color.R, color.G, color.B)
    if keyboard is None:
        raise Exception("Keyboard not found")
    if keys == "all":
        keyboard.set_color(color)
    else:
        if not human:
            keys = keys.split(',')
            keys = [int(key) for key in keys]
            for key in keys:
                keyboard.leds[key].set_color(color)