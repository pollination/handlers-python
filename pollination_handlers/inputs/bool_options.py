"""Handlers to convert various boolean options to boolean flag strings."""
from .helper import bool_option_to_str


def filter_des_days_to_str(value):
    """Translate a boolean to the filter_des_days flag.

        Args:
            value: Either a boolean or one of two text strings.

            * filter-des-days
            * all-des-days

        Returns:
            str -- filter_des_days flag text.
    """
    return bool_option_to_str(
        value, ('filter-des-days', 'all-des-days'), 'filter_des_days'
    )


def skip_overture_to_str(value):
    """Translate a boolean to the skip_overture flag.

        Args:
            value: Either a boolean or one of two text strings.

            * skip-overture
            * overture

        Returns:
            str -- skip_overture flag text.
    """
    return bool_option_to_str(value, ('skip-overture', 'overture'), 'skip_overture')


def glare_control_devices_to_str(value):
    """Translate a boolean to the glare_control_devices flag.

        Args:
            value: Either a boolean or one of two text strings.

            * glare-control
            * no-glare-control

        Returns:
            str -- glare_control_devices flag text.
    """
    return bool_option_to_str(
        value, ('glare-control', 'no-glare-control'), 'glare_control_devices'
    )


def use_multiplier_to_str(value):
    """Translate a boolean to the use_multiplier flag.

        Args:
            value: Either a boolean or one of two text strings.

            * multiplier
            * full-geometry

        Returns:
            str -- use_multiplier flag text.
    """
    return bool_option_to_str(value, ('multiplier', 'full-geometry'), 'use_multiplier')


def is_residential_to_str(value):
    """Translate a boolean to the is_residential flag.

        Args:
            value: Either a boolean or one of two text strings.

            * residential
            * nonresidential

        Returns:
            str -- is_residential flag text.
    """
    return bool_option_to_str(value, ('residential', 'nonresidential'), 'is_residential')


def write_set_map_to_str(value):
    """Translate a boolean to the write_set_map flag.

        Args:
            value: Either a boolean or one of two text strings.

            * write-op-map
            * write-set-map

        Returns:
            str -- write_set_map flag text.
    """
    return bool_option_to_str(value, ('write-set-map', 'write-op-map'), 'write_set_map')
