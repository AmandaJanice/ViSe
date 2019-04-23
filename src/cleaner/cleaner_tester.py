import handler as cleaner

if __name__ == '__main__':
    # Testing

    print(cleaner.id_not_defined("some_id"))
    print(cleaner.id_saved("another_id"))
    text = "\"text with brackets\""
    print(text)
    print(cleaner.string_cleaner(text))
    print(cleaner.string_cleaner(234))
