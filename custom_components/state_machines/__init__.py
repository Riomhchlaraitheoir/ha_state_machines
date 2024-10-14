from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from .const import DOMAIN

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    data = hass.data.setdefault(DOMAIN, {})

    # config_entry.add_update_listener() TODO
    return True
