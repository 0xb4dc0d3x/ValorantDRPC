from ...localization.localization import Localizer


def presence(rpc, client=None, data=None, content_data=None, config=None):
    rpc.update(
        state=Localizer.get_localized_text("presences", "startup", "loading"),
        large_image="game_icon",
        large_text="VALORANTDRPC",
        buttons=[{
            'label': Localizer.get_localized_text("presences", "startup", "view_github"),
            'url': "https://github.com/0xb4dc0d3x/ValorantDRPC/releases"
        }] if Localizer.get_config_value("startup", "show_github_link") else None
    )
