"""Handlers for validating Radiance parameters."""

rtrace_options = [
    '-f', '-o', '-te', '-ti', '-tE', '-tI', '-i', '-I', '-u', '-h',
    '-x', '-y', '-n', '-dj', '-ds', '-dt', '-dc', '-dr', '-dp', '-dv',
    '-ss', '-st', '-bv', '-ld', '-av', '-aw', '-ab', '-ar', '-aa', '-ad',
    '-as', '-af', '-ae', '-ai', '-aE', '-aI', '-ap', '-am', '-ac', '-aC',
    '-me', '-ma', '-mg', '-ms', '-lr', '-lw', '-e', '-w', '-P', '-PP'
]

rcontrib_options = [
    '-n', '-V', '-c', '-fo', '-r', '-e', '-f', '-o', '-p', '-b', '-bn', '-m', '-M'
] + rtrace_options

rpict_options = [
    '-vt', '-vp', '-vd', '-vu', '-vh', '-vv', '-vo', '-va', '-vs', '-vl',
    '-vf', '-x', '-y', '-pa', '-ps', '-pt', '-pj', '-pm', '-pd', '-dj',
    '-ds', '-dt', '-dc', '-dr', '-dp', '-dv', '-ss', '-st', '-bv', '-av', '-aw',
    '-ab', '-ar', '-aa', '-ad', '-as', '-af', '-ae', '-ai', '-aE', '-aI',
    '-ap', '-am', '-ac', '-aC', '-me', '-ma', '-mg', '-ms', '-i', '-u', '-lr', '-lw',
    '-S', '-o', '-r', '-ro', '-z', '-P', '-PP', '-t', '-e', '-w'
]

multi_value_options = {
    '-ap': (1, 3),
    '-av': (3, 3),
    '-me': (3, 3),
    '-ma': (3, 3),
    '-vp': (3, 3),
    '-vd': (3, 3),
    '-vu': (3, 3)
}

accelerad_options = ['-g', '-gv', '-al', '-ag', '-az', '-ac', '-an', '-at', '-ax']

# Extend with Accelerad options
rtrace_options.extend(accelerad_options)
rcontrib_options.extend(accelerad_options)
rpict_options.extend(accelerad_options)


def validate_input_output(option, rad_options):
    valid_suffixes = {'a', 'f', 'd', 'c'}
    suffix = option[2:]

    if len(suffix) == 2 and all(c in valid_suffixes for c in suffix):
        if option[0:2] not in rad_options:
            raise ValueError(f'Invalid option detected: {option}')
    else:
        raise ValueError(f'Invalid option detected: {option}')


def validate_view_type(option, rad_options):
    valid_suffixes = {'v', 'l', 'c', 'h', 'a', 's'}
    suffix = option[3:]
    if len(suffix) == 1 and suffix in valid_suffixes:
        if '-vt' not in rad_options:
            raise ValueError(f'Invalid option detected: {option}')
    else:
        raise ValueError(f'Invalid option detected: {option}')


def validate_rtrace_params(input_params):
    input_list = input_params.split()
    i = 0
    while i < len(input_list):
        option = input_list[i]

        if option.startswith('-f') and len(option) == 4:
            validate_input_output(option, rtrace_options)
            i += 1
        elif option not in rtrace_options:
            raise ValueError(f'Invalid option detected: {option}')
        elif option in multi_value_options:
            min_args, max_args = multi_value_options[option]
            remaining_args = len(input_list) - (i + 1)
            if remaining_args < min_args:
                raise ValueError(
                    f'Option {option} expects at least {min_args} values but got fewer.')
            if remaining_args > max_args:
                remaining_args = max_args
            i += 1 + remaining_args
        else:
            if i + 1 < len(input_list) and input_list[i + 1] not in rtrace_options:
                i += 2
            else:
                i += 1


def validate_rcontrib_params(input_params):
    input_list = input_params.split()
    i = 0
    while i < len(input_list):
        option = input_list[i]

        if option.startswith('-f') and len(option) == 4:
            validate_input_output(option, rcontrib_options)
            i += 1
        elif option not in rcontrib_options:
            raise ValueError(f'Invalid option detected: {option}')
        elif option in multi_value_options:
            min_args, max_args = multi_value_options[option]
            remaining_args = len(input_list) - (i + 1)
            if remaining_args < min_args:
                raise ValueError(
                    f'Option {option} expects at least {min_args} values but got fewer.')
            if remaining_args > max_args:
                remaining_args = max_args
            i += 1 + remaining_args
        else:
            if i + 1 < len(input_list) and input_list[i + 1] not in rcontrib_options:
                i += 2
            else:
                i += 1


def validate_rpict_params(input_params):
    input_list = input_params.split()
    i = 0
    while i < len(input_list):
        option = input_list[i]

        if option.startswith('-vt') and len(option) == 4:
            validate_view_type(option, rpict_options)
            i += 1
        elif option not in rpict_options:
            raise ValueError(f'Invalid option detected: {option}')
        elif option in multi_value_options:
            min_args, max_args = multi_value_options[option]
            remaining_args = len(input_list) - (i + 1)
            if remaining_args < min_args:
                raise ValueError(
                    f'Option {option} expects at least {min_args} values but got fewer.')
            if remaining_args > max_args:
                remaining_args = max_args
            i += 1 + remaining_args
        else:
            if i + 1 < len(input_list) and input_list[i + 1] not in rpict_options:
                i += 2
            else:
                i += 1

# Example usage:
if __name__ == '__main__':
    test_input = '-vta -ab 4 -ap file1 50 100 -ad 5000 -av 0.2 0.5 0.8'
    validate_rpict_params(test_input)
