INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)


class InvalidPasswordError(KeyError):
    pass


class InvalidUsernameError(KeyError):
    pass


def validate_password(username, password):
    try:
        if (password == username):
            raise InvalidUsernameError
        if (password in INVALID_PASSWORDS):
            raise InvalidPasswordError

    except InvalidPasswordError:
        "Password is invalid"
    except InvalidUsernameError:
        "Username is same as password"
    else:
        return True


def create_account(username, password):
    print(f"Account for {username} created")
    return (username, password)


def main(username, password):
    valid = validate_password(username, password)

    if valid:
        account = create_account(username, password)
    else:
        print("Oh no!")


if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!