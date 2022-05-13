import user
import product
import review


def main():
    brianna = user.User(1, 'Brianna')
    mary = user.User(2, 'Mary')

    keyboard = brianna.sell_product('Keyboard', 'A nice mechanical keyboard', 100)
    print(keyboard.available)  # => True
    mary.buy_product(keyboard)
    print(keyboard.available)  # => False
    review = mary.write_review('This is the best keyboard ever!', keyboard)
    print(review in mary.reviews)  # => True
    print(review in keyboard.reviews)  # => True

if __name__ == "__main__":
    main()