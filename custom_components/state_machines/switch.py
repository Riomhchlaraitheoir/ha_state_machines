from typing import Any

from homeassistant.components.switch import SwitchEntity, SwitchDeviceClass
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


def setup_platform(
        hass: HomeAssistant,
        config: ConfigType,
        add_entities: AddEntitiesCallback,
        discovery_info: DiscoveryInfoType | None = None
) -> None:
    add_entities([EnabledSwitch()])

class EnabledSwitch(SwitchEntity):
    _attr_name = "Enabled"
    _attr_device_class = SwitchDeviceClass.SWITCH

    def turn_on(self, **kwargs: Any) -> None:
        self.is_on = True

    def turn_off(self, **kwargs: Any) -> None:
        self.is_on = False

    def toggle(self, **kwargs: Any) -> None:
        self.is_on = not self.is_on

