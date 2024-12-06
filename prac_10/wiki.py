import wikipedia


def get_wikipedia_page():
    title = input("Enter page title: ")

    while title:
        try:
            page = wikipedia.summary(title)
            print(f"Title: {page.title}")
            print(f"Summary: {page.summary}")
            print(f"URL: {page.url}")
        except wikipedia.exceptions.PageError:
            print(f"Page id \"{title}\" does not match any pages. Try another id!")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"We need a more specific title. Try one of the following, or a new search:\n{e.options}")

        title = input("Enter page title: ")

    print("Thank you.")


if __name__ == "__main__":
    get_wikipedia_page()
